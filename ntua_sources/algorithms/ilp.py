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
        
        return {'statusCode':self.model.status,'status':LpStatus[self.model.status],'variables':self.model.variables()}
        
    def solve(self):
        self.model = LpProblem(name="minVertexCover", sense=LpMinimize)
        
        activation = LpVariable.dicts("activation",(n for n in self.graph.nodes),cat='Integer',lowBound=0)
        transfered = LpVariable.dicts("transfered",(edge for edge in self.graph.edges),cat='Integer',lowBound=0)
                
        # for n in self.graph: 
            # for tempn,d in self.graph.edges(n):
                # self.model += transfered[(n,d)] <= self.graph.edges[n,d]['capacity']*activation[n]*5
        
        for n in self.graph: 
            self.model += lpSum([transfered[edge] for edge in self.graph.edges if edge[0] == n or edge[1] == n]) >= self.volume
        
        for edge in self.graph.edges:
            self.model += transfered[edge] <= self.volume*(activation[edge[0]]+activation[edge[1]])*self.graph.number_of_nodes()
            # self.model += transfered[edge] <= self.graph.edges[edge]['capacity']*(activation[edge[0]]+activation[edge[1]])*5

        #An = activation, self.volume = V , capacity W
        self.model += lpSum(
            [activation[n]*self.volume for n in self.graph] + 
            [transfered[edge]*(1/self.graph.edges[edge[0],edge[1]]['capacity']) for edge in self.graph.edges]
        )
        
        status = self.model.solve()
        
        print(f"status: {self.model.status}, {LpStatus[self.model.status]}")
        print(f"objective: {self.model.objective.value()}")
        for var in self.model.variables():
            print(f"{var.name}: {var.value()}")
        print()
        for name, constraint in self.model.constraints.items():
            print(f"{name}: {constraint.value()}")
        print()
        
        return {'statusCode':self.model.status,'status':LpStatus[self.model.status],'variables':self.model.variables()}