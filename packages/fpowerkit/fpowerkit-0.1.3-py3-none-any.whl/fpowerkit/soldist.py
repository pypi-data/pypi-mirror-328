from gurobipy import GRB, Constr, LinExpr, Model, Var
from gurobipy import quicksum as Qs
from pathlib import Path
from typing import Optional, Union
from dataclasses import dataclass
import warnings, math
from .solbase import *

VF = Union[Var, float]

@dataclass
class LoadReduceModule:
    '''Load Reduce module'''
    Bus:BusID
    Limit:TimeFunc
    Reduction:FloatVar = None

class DistFlowSolver(SolverBase):
    '''DistFlow solver'''
    def __init__(self, grid:Grid, eps:float = 1e-6, default_saveto:str = DEFAULT_SAVETO, /, *, mlrp:float = 0.5):
        '''
        Initialize
            grid: Grid object
            default_saveto: Default path to save the results
            mlrp: Maximum proportion of load reduction
        '''
        super().__init__(grid, eps, default_saveto)
        self._decb:dict[BusID, LoadReduceModule] = {}
        self.C = 1e9
        self._mlrp = mlrp
    
    @property
    def MLRP(self):
        '''Get the maximum load reduction proportion'''
        return self._mlrp
    @MLRP.setter
    def MLRP(self, v:float):
        '''Set the maximum load reduction proportion'''
        if v < 0 or v > 1:
            raise ValueError("Invalid maximum load reduction proportion")
        self._mlrp = v
    
    def AddReduce(self, bus:BusID, limit:TimeFunc, reduction:Optional[FloatVar] = None):
        '''Add a load reduction module'''
        self._decb[bus] = LoadReduceModule(bus, limit, reduction)
    
    def RemoveReduce(self, bus:BusID):
        '''Remove a load reduction module'''
        if bus in self._decb:
            del self._decb[bus]
        
    def GetReduce(self, bus:BusID) -> LoadReduceModule:
        '''Get the load reduction module'''
        return self._decb[bus]
    
    @property
    def DecBuses(self):
        return self._decb
    
    def solve(self, _t: int, /, *, timeout_s:float = 1) -> 'tuple[GridSolveResult, float]':
        '''Get the best result at time _t, return a tuple: (result status, optimal objective value)'''
        ok, val = self.__solve(_t, False, False, timeout_s)
        if ok == GRB.Status.OPTIMAL:
            return GridSolveResult.OK, val
        else:
            ok, val = self.__solve(_t, True, True, timeout_s)
            if ok == GRB.Status.OPTIMAL:
                return GridSolveResult.OKwithoutVICons, val
            elif ok == GRB.Status.SUBOPTIMAL:
                return GridSolveResult.SubOKwithoutVICons, val
            else:
                print(f"Failed to solve at time {_t}: {ok}")
                if self.saveto != "":
                    p = Path(self.saveto)
                    p.mkdir(parents=True, exist_ok=True)
                    self.grid.savePQofBus(str(p/f"{_t}_load.csv"), _t)
                return GridSolveResult.Failed, val            
        
    def __solve(self, _t: int, relax_V: bool, relax_I: bool, timeout_s:float) -> 'tuple[int, float]':
        model = Model("model")
        
        ''' ---------Variables----------
        pg0[k]: Generator active power
        qg0[k]: Generator reactive power
        pvwp[k]: PVWind active power
        --> pg[j]: Active power of all generators at the bus
        --> qg[j]: Reactive power of all generators at the bus
        v[j]: Bus voltage ** 2
        l[i,j]: Line current ** 2
        P[i,j]: Line active power
        Q[i,j]: Line reactive power
        '''

        # Create GEN vars
        pg0: dict[str, VF] = {}
        qg0: dict[str, VF] = {}
        for g in self.grid.Gens:
            if g.FixedP:
                assert g.P is not None
                pg0[g.ID] = g.P(_t) if isinstance(g.P, TimeFunc) else g.P
            elif g.Pmin is not None and g.Pmax is not None:
                pg0[g.ID] = model.addVar(name=f"pg_{g.ID}", vtype='C', lb=g.Pmin(_t), ub=g.Pmax(_t))
            else:
                raise ValueError(f"Generator {g.ID} provides neither P or (pmin, pmax)")
            if g.FixedQ:
                assert g.Q is not None
                qg0[g.ID] = g.Q(_t) if isinstance(g.Q, TimeFunc) else g.Q
            elif g.Qmin is not None and g.Qmax is not None:
                qg0[g.ID] = model.addVar(name=f"qg_{g.ID}", vtype='C', lb=g.Qmin(_t), ub=g.Qmax(_t))
            else:
                raise ValueError(f"Generator {g.ID} provides neither Q or (qmin, qmax)")
        
        pvwp: dict[str, Var] = {p.ID: model.addVar(
            name=f"pvw_{p.ID}", vtype='C', lb=0, ub=p.P(_t)
        ) for p in self.grid.PVWinds}
        pvwq: dict[str, Var] = {p.ID: model.addVar(
            name=f"pvw_{p.ID}", vtype='C', lb=-GRB.INFINITY, ub=GRB.INFINITY
        ) for p in self.grid.PVWinds}

        # Bind GEN vars to Bus
        pg: dict[str, list[VF]] = {bus.ID: [] for bus in self.grid.Buses}
        qg: dict[str, list[VF]] = {bus.ID: [] for bus in self.grid.Buses}
        pd: dict[str, float] = {bus.ID: bus.Pd(_t) for bus in self.grid.Buses}
        qd: dict[str, float] = {bus.ID: bus.Qd(_t) for bus in self.grid.Buses}
        for g in self.grid.Gens:
            pg[g.BusID].append(pg0[g.ID])
            qg[g.BusID].append(qg0[g.ID])
        for p in self.grid.PVWinds:
            pg[p.BusID].append(pvwp[p.ID])
            qg[p.BusID].append(pvwq[p.ID])
        for e in self.grid.ESSs:
            p, q = e.GetLoad(_t, self.grid.ChargePrice(_t), self.grid.DischargePrice(_t))
            e.P = p
            if p > 0:
                pg[e.BusID].append(p)
                qg[e.BusID].append(q)
            elif p < 0:
                pd[e.BusID] -= p
                qd[e.BusID] -= q
        
        # Create BUS vars
        has_slack = 0
        v = {bus.ID: model.addVar(name=f"v_{bus.ID}", vtype='C') for bus in self.grid.Buses}
        dvmin = {}
        dvmax = {}
        for bus in self.grid.Buses:
            bid = bus._id
            if bus.FixedV:
                assert bus.V is not None, f"Bus {bid} has fixed voltage but not set"
                model.addConstr(v[bid] == bus.V ** 2)
                has_slack += 1
            elif relax_V:
                dvmin[bid] = model.addVar(name=f"dvmin_{bid}", vtype='C', lb=0)
                dvmax[bid] = model.addVar(name=f"dvmax_{bid}", vtype='C', lb=0)
                model.addConstr(v[bid] >= bus.MinV ** 2 - dvmin[bid])
                model.addConstr(v[bid] <= bus.MaxV ** 2 + dvmax[bid])
            else:
                v[bid].LB = bus.MinV ** 2
                v[bid].UB = bus.MaxV ** 2

        if has_slack == 0:
            raise ValueError("No slack bus found.")
        elif has_slack > 1:
            warnings.warn("More than 1 slack bus. May lead to unfeasible result.")
        
        # Create Line vars
        dlmax = {}
        if relax_I:
            l = {line.ID: model.addVar(name=f"l_{line.ID}", vtype='C', lb=0) for line in self.grid.Lines}
            for line in self.grid.Lines:
                dlmax[line.ID] = model.addVar(name=f"dlmax_{line.ID}", vtype='C', lb=0)
                model.addConstr(l[line.ID] <= (line.max_I/self.grid.Ib) ** 2 + dlmax[line.ID])
        else:
            l = {line.ID: model.addVar(
                name=f"l_{line.ID}", vtype='C', lb=0, ub=(line.max_I/self.grid.Ib) ** 2
            ) for line in self.grid.Lines}
        
        P = {line.ID: model.addVar(name=f"P_{line.ID}", vtype='C', lb=-GRB.INFINITY, ub=GRB.INFINITY) for line in
             self.grid.Lines}
        Q = {line.ID: model.addVar(name=f"Q_{line.ID}", vtype='C', lb=-GRB.INFINITY, ub=GRB.INFINITY) for line in
             self.grid.Lines}
        
        Pdec = {bus: model.addVar(name=f"Pdec_{bus}", vtype='C', 
            lb=0, ub=lim.Limit(_t) * self._mlrp) for bus,lim in self._decb.items()}
        
        # ----------Constraints-----------
        Pcons: dict[str, Constr] = {}
        Qcons: dict[str, Constr] = {}

        for bus in self.grid.Buses:
            j = bus.ID
            flow_in = self.grid.LinesOfTBus(j)
            flow_out = self.grid.LinesOfFBus(j)
            dec = Pdec[j] if j in self._decb else 0
            Pcons[j] = model.addConstr(Qs(P[ln.ID] - ln.R * l[ln.ID] for ln in flow_in) + Qs(pg[j]) == Qs(
                P[ln.ID] for ln in flow_out) + pd[j] - dec, f"Pcons_{j}")
            Qcons[j] = model.addConstr(Qs(Q[ln.ID] - ln.X * l[ln.ID] for ln in flow_in) + Qs(qg[j]) == Qs(
                Q[ln.ID] for ln in flow_out) + qd[j], f"Qcons_{j}")

        for line in self.grid.Lines:
            i, j = line.pair
            lid = line.ID
            model.addConstr(
                v[j] == v[i] - 2 * (line.R * P[lid] + line.X * Q[lid]) + (line.R ** 2 + line.X ** 2) * l[lid],
                f"ΔU2_cons_{lid}")
            model.addConstr(P[lid] ** 2 + Q[lid] ** 2 <= l[lid] * v[i], f"SoC_cons_{lid}")
        
        for p in self.grid.PVWinds:
            model.addConstr(pvwp[p.ID] * math.sqrt(1 - p.PF**2) == pvwq[p.ID])

        decs = self.C * (Qs(Pdec.values()) + Qs(dvmin.values()) + Qs(dvmax.values()) + Qs(dlmax.values()))
        crpe = Qs(p.CC*(p.P(_t)-pvwp[p.ID]) for p in self.grid.PVWinds)
        goal = Qs(g.CostA(_t) * pg0[g.ID] ** 2 + g.CostB(_t) * pg0[g.ID] + g.CostC(_t) for g in self.grid.Gens)

        model.setObjective(decs + goal + crpe, GRB.MINIMIZE)
        model.setParam(GRB.Param.OutputFlag, 0)
        model.setParam(GRB.Param.QCPDual, 1)
        model.setParam(GRB.Param.TimeLimit, timeout_s)
        model.setParam(GRB.Param.OptimalityTol, 1e-6)
        model.update()
        model.optimize()
        if model.Status != GRB.Status.OPTIMAL:
            return model.Status, -1

        for bus in self.grid.Buses:
            j = bus.ID
            bus.V = v[j].X ** 0.5
            try:
                sp = Pcons[j].Pi
            except:
                sp = None if not self.grid._holdShadowPrice else bus.ShadowPrice
            bus.ShadowPrice = sp

        for line in self.grid.Lines:
            lid = line.ID
            line.I = l[lid].X ** 0.5
            line.P = P[lid].X
            line.Q = Q[lid].X

        for gen in self.grid.Gens:
            j = gen.ID
            p = pg0[j]
            if isinstance(p, Var): gen._p = p.X
            q = qg0[j]
            if isinstance(q, Var): gen._q = q.X
        
        for p in self.grid.PVWinds:
            p._pr = pvwp[p.ID].X
            p._qr = pvwq[p.ID].X
            pgen = p.P(_t)
            p._cr = 1 - p._pr / pgen if pgen > 0 else 0
            
        for bus,lim in self._decb.items():
            lim.Reduction = Pdec[bus].X
            if lim.Reduction < 1e-8: lim.Reduction = 0

        return model.Status, goal.getValue()