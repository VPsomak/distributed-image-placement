#	This file is part of Distributed Image Placer.
#
#    Distributed Image Placer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Distributed Image Placer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Distributed Image Placer.  If not, see https://www.gnu.org/licenses/.

from pulp import LpMinimize, LpProblem, LpStatus, LpVariable, lpSum

class ilp_model:
    
    def __init__(self,graph,volume):
        self.graph=graph
        self.volume=volume
    
    def solve1(self):
        self.model = LpProblem(name="minVertexCover", sense=LpMinimize)
        activation = LpVariable.dicts("activation",(nodeIndex for nodeIndex in range(self.graph.number_of_nodes())),cat='Binary')
        self.model += lpSum([activation[n]*(self.volume/self.graph[n][d]['capacity']) for n in range(self.graph.number_of_nodes()) for d in range(self.graph.number_of_nodes()) if d != n and n in self.graph and d in self.graph[n]]) >= 0.001
        self.model += lpSum([activation[n]*(self.volume/self.graph[n][d]['capacity']) for n in range(self.graph.number_of_nodes()) for d in range(self.graph.number_of_nodes()) if d != n and n in self.graph and d in self.graph[n]])
        print(self.model)
        print()
        
        status = self.model.solve()
        print(f"status: {self.model.status}, {LpStatus[self.model.status]}")
        print(f"objective: {self.model.objective.value()}")
        for var in self.model.variables():
            print(f"{var.name}: {var.value()}")
        print()
        for name, constraint in self.model.constraints.items():
            print(f"{name}: {constraint.value()}")
        print()
        
    def solve(self):
        self.model = LpProblem(name="minVertexCover", sense=LpMinimize)
        
        activation = LpVariable.dicts("activation",(nodeIndex for nodeIndex in range(self.graph.number_of_nodes())),cat='Binary')
        transfered = LpVariable.dicts("transfered",((n,d) for n,d in self.graph.edges),cat='Integer',lowBound=0)
        
        total_caps = []
        for n in range(self.graph.number_of_nodes()):
            if n in self.graph:
                total_cap = 0.0
                for d in self.graph[n]:
                    total_cap += self.graph[n][d]['capacity']
                total_caps.append(total_cap)
        #Δεν δουλεύει το self.graph[n], άλλαξτο σε graph.edges με κάποιο τρόπο.
        for n in self.graph:
            self.model += lpSum([transfered[(n,d)] for d in self.graph[n]]) <= total_caps[n]*activation[n]*3
        
        for d in range(self.graph.number_of_nodes()):
            self.model += lpSum([transfered[(n,d)] for n in self.graph if d in self.graph[n]]) == self.volume
            
        for n in self.graph:
            for d in self.graph[n]:
                self.model += transfered[(n,d)] <= self.volume*activation[n]
        
        self.model += lpSum(
            [activation[n]*self.volume for n in range(self.graph.number_of_nodes())] + 
            [transfered[(n,d)]*(1/self.graph[n][d]['capacity']) for n in self.graph for d in self.graph[n]]
        )
        
        status = self.model.solve()
        return {'statusCode':self.model.status,'status':LpStatus[self.model.status],'variables':self.model.variables()}