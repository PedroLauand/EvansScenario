def d(x,y):
    if x==y :
        return 1
    elif x !=y :
        return 0
def EvansBehaviorCheckA3(p):
    import gurobipy as gp
    import numpy as np
    import Indices as ind  
#Here we are going to implement the CCP for the evans scenario where alice has |A|=3 and |B|=|C|=2.

    m = gp.Model()
#Joint distribution 
    q=m.addMVar(72,lb=0,ub=1)

#Auxiliary variables 
    z_AC=m.addMVar(36,lb=0,ub=1)
    z_A=m.addMVar(9,lb=0,ub=1)
    z_C=m.addMVar(4,lb=0,ub=1)

    obj=1
    m.Params.NonConvex=2
    m.Params.OutputFlag=0
    m.setObjective(obj, gp.GRB.MINIMIZE)
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
    for c in range(2):
        for b in range(2):
            for a in range(3):
                l=[]
                for c1 in range(2):
                    for c0 in range(2):
                        for b_ in range(2):
                            for a1 in range(3):
                                for a0 in range(3):
                                    alpha=[a0,a1]
                                    gamma=[c0,c1]
                                    l=np.append(l,d(a,alpha[b])*d(b,b_)*d(c,gamma[b]))
                M=np.append(M,l)
    M=np.reshape(M,(12,72))
    m.addConstr(M@q==p)
    
    m.optimize()
    status = m.status
    if status==gp.GRB.OPTIMAL:
        
        return "classical"
    else:
        print(status==gp.GRB.INFEASIBLE,status)
        return "non-classical"

def pQ_Inst(state,A0,A1,A2,B0,B1,q):
    import numpy as np
    A=[A0,A1,A2]
    B=[B0,B1]
    p=[]
    
    for b in range(2):
        for a in range(2):
            for x in range(3):
                p=np.append(p,q[x]*np.trace(state@np.kron(A[x][a],B[a][b])))

    p=np.real(p)
    return p
def EvansBehaviorCheckA4(p):
    import gurobipy as gp
    import numpy as np
    import Indices as ind  
#Here we are going to implement the CCP for the evans scenario where alice has |A|=4 and |B|=|C|=2.

    m = gp.Model()
#Joint distribution 
    q=m.addMVar(128,lb=0,ub=1)

#Auxiliary variables 
    z_AC=m.addMVar(64,lb=0,ub=1)
    z_A=m.addMVar(16,lb=0,ub=1)
    z_C=m.addMVar(4,lb=0,ub=1)

    obj=1
    m.Params.NonConvex=2
    m.Params.OutputFlag=0
    m.setObjective(obj, gp.GRB.MINIMIZE)
    for c1 in range(2):
        for c0 in range(2):
            for a1 in range(4):
                for a0 in range(4):
                    m.addConstr(z_AC[ind.evansmarginalA4(a0,a1,c0,c1)]==q[ind.evansA4(a0,a1,0,c0,c1)]+q[ind.evansA4(a0,a1,1,c0,c1)])
    
    for a1 in range(4):
        for a0 in range(4):
            m.addConstr(z_A[ind.evansAmarginalA4(a0,a1)]==z_AC[ind.evansmarginalA4(a0,a1,0,0)]+z_AC[ind.evansmarginalA4(a0,a1,1,0)]+z_AC[ind.evansmarginalA4(a0,a1,0,1)]+z_AC[ind.evansmarginalA4(a0,a1,1,1)])
    for c1 in range(2):
        for c0 in range(2):
            m.addConstr(z_C[ind.evansCmarginalA4(c0,c1)]==z_AC[ind.evansmarginalA4(0,0,c0,c1)]+z_AC[ind.evansmarginalA4(1,0,c0,c1)]+z_AC[ind.evansmarginalA4(2,0,c0,c1)]+z_AC[ind.evansmarginalA4(3,0,c0,c1)]+z_AC[ind.evansmarginalA4(0,1,c0,c1)]+z_AC[ind.evansmarginalA4(1,1,c0,c1)]+z_AC[ind.evansmarginalA4(2,1,c0,c1)]+z_AC[ind.evansmarginalA4(3,1,c0,c1)]+z_AC[ind.evansmarginalA4(0,2,c0,c1)]+z_AC[ind.evansmarginalA4(1,2,c0,c1)]+z_AC[ind.evansmarginalA4(2,2,c0,c1)]+z_AC[ind.evansmarginalA4(3,2,c0,c1)]+z_AC[ind.evansmarginalA4(0,3,c0,c1)]+z_AC[ind.evansmarginalA4(1,3,c0,c1)]+z_AC[ind.evansmarginalA4(2,3,c0,c1)]+z_AC[ind.evansmarginalA4(3,3,c0,c1)])

    for c1 in range(2):
        for c0 in range(2):
            for a1 in range(4):
                for a0 in range(4):
                    m.addConstr(z_AC[ind.evansmarginalA4(a0,a1,c0,c1)]==z_A[ind.evansAmarginalA4(a0,a1)]@z_C[ind.evansCmarginalA4(c0,c1)])
    M=[]
    for c in range(2):
        for b in range(2):
            for a in range(4):
                l=[]
                for c1 in range(2):
                    for c0 in range(2):
                        for b_ in range(2):
                            for a1 in range(4):
                                for a0 in range(4):
                                    alpha=[a0,a1]
                                    gamma=[c0,c1]
                                    l=np.append(l,d(a,alpha[b])*d(b,b_)*d(c,gamma[b]))
                M=np.append(M,l)
    M=np.reshape(M,(16,128))
    m.addConstr(M@q==p)
    
    m.optimize()
    status = m.status
    if status==gp.GRB.OPTIMAL:
        
        return "classical"
    else:
        print(status==gp.GRB.INFEASIBLE,status)
        return "non-classical"
