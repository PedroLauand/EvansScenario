
import gurobipy as gp
import numpy as np
import Indices as ind  
from EvansA3Gurobi import *
from scipy.stats import unitary_group
#We can optimize multilinear problems with GUROBI as well !! 
#Here we are going to optimize the Kdagni's inequality for the evans senario.
def d(x,y):
    if x==y :
        return 1
    elif x !=y :
        return 0


m = gp.Model()
#Joint distribution 
q=m.addMVar(72,lb=0,ub=1)

#Auxiliary variables 
z_AC=m.addMVar(36,lb=0,ub=1)
z_A=m.addMVar(9,lb=0,ub=1)
z_C=m.addMVar(4,lb=0,ub=1)
#Observable distribution p(x,a,b) as a variable and p(x) as a variable.
p=m.addMVar(12,lb=0,ub=1) 
p_x=m.addMVar(3,lb=0,ub=1)



m.Params.NonConvex=2
m.Params.OutputFlag=1

for c1 in range(2):
    for c0 in range(2):
        for a1 in range(3):
            for a0 in range(3):
                m.addConstr(z_AC[ind.evansmarginalA3(a0,a1,c0,c1)]==q[ind.evansA3(a0,a1,0,c0,c1)]+q[ind.evansA3(a0,a1,1,c0,c1)])

for a1 in range(3):
    for a0 in range(3):
        m.addConstr(z_A[ind.evansAmarginalA3(a0,a1)]==z_AC[ind.evansmarginalA3(a0,a1,0,0)]+z_AC[ind.evansmarginalA3(a0,a1,1,0)]+z_AC[ind.evansmarginalA3(a0,a1,0,1)]+z_AC[ind.evansmarginalA3(a0,a1,1,1)])
for c1 in range(2):
    for c0 in range(2):
        m.addConstr(z_C[ind.evansCmarginalA3(c0,c1)]==z_AC[ind.evansmarginalA3(0,0,c0,c1)]+z_AC[ind.evansmarginalA3(1,0,c0,c1)]+z_AC[ind.evansmarginalA3(2,0,c0,c1)]+z_AC[ind.evansmarginalA3(0,1,c0,c1)]+z_AC[ind.evansmarginalA3(1,1,c0,c1)]+z_AC[ind.evansmarginalA3(2,1,c0,c1)]+z_AC[ind.evansmarginalA3(0,2,c0,c1)]+z_AC[ind.evansmarginalA3(1,2,c0,c1)]+z_AC[ind.evansmarginalA3(2,2,c0,c1)])

for c1 in range(2):
    for c0 in range(2):
        for a1 in range(3):
            for a0 in range(3):
                m.addConstr(z_AC[ind.evansmarginalA3(a0,a1,c0,c1)]==z_A[ind.evansAmarginalA3(a0,a1)]@z_C[ind.evansCmarginalA3(c0,c1)])
M=[]
for b in range(2):
    for a in range(2):
        for x in range(3):
            l=[]
            for c1 in range(2):
                for c0 in range(2):
                    for b_ in range(2):
                        for a1 in range(3):
                            for a0 in range(3):
                                alpha=[a0,a1]
                                gamma=[c0,c1]
                                l=np.append(l,d(x,alpha[a])*d(a,b_)*d(b,gamma[b]))
            M=np.append(M,l)
M=np.reshape(M,(12,72))
m.addConstr(M@q==p)
for x in range(3):
    m.addConstr(p_x[x]==p[ind.evansObIndexA3(x,0,0)]+p[ind.evansObIndexA3(x,1,0)]+p[ind.evansObIndexA3(x,0,1)]+p[ind.evansObIndexA3(x,1,1)])


#Auxiliary prod variables 
prod_x=m.addMVar(3,lb=0,ub=1)
m.addConstr(prod_x[0]==p_x[1]@p_x[2])
m.addConstr(prod_x[1]==p_x[0]@p_x[2])
m.addConstr(prod_x[2]==p_x[0]@p_x[1])
#Objective function: p(a=0,b= 1, x=0)p(x = 1)p(x = 2) −p(a=0, b=1,x= 1)p(x = 0)p(x = 2) −p(a=1, b=1, x=1)p(x = 0)p(x = 2)−p(a=1, b=0, x=2)p(x = 0)p(x = 1) −p(a=0, b=1, x=2)p(x = 0)p(x = 1) ≤0

obj=p[ind.evansObIndexA3(0,0,1)]@prod_x[0]-p[ind.evansObIndexA3(1,0,1)]@prod_x[1]-p[ind.evansObIndexA3(1,1,1)]@prod_x[1]-p[ind.evansObIndexA3(2,1,0)]@prod_x[2]-p[ind.evansObIndexA3(2,0,1)]@prod_x[2]

m.setObjective(obj, gp.GRB.MAXIMIZE)
m.optimize()
status = m.status
ob = m.getObjective()
print(ob.getValue())
#0.037037679304398934
