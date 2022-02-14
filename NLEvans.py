def d(x,y):
    if x==y :
        return 1
    elif x !=y :
        return 0
def NLEvans(p):
    import gurobipy as gp
    import numpy as np
    import Indices as ind  
    #Here we optimize the distance to a given point to the set of classical correlations. 
#the output is the maximal distance v such that pv=vp+(1-v)1/12 is classical. This is for the case where |A|=|B|=2 and |X|=3.


    m = gp.Model()
#Joint distribution 
    q=m.addMVar(72,lb=0,ub=1)

#Auxiliary variables 
    z_AC=m.addMVar(36,lb=0,ub=1)
    z_A=m.addMVar(9,lb=0,ub=1)
    z_C=m.addMVar(4,lb=0,ub=1)

    v=m.addMVar(1,lb=0,ub=1)
    pv=m.addMVar(12,lb=0,ub=1)

    for i in range(12):
       m.addConstr(pv[i]==v[0]*p[i]+(1-v[0])*1/12)
    
    #obj=1
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
    m.addConstr(M@q==pv)
    obj=1*v[0]

    m.setObjective(obj, gp.GRB.MAXIMIZE)
    m.optimize()
    status = m.status

    if status==gp.GRB.OPTIMAL:
        v=v.X
        return v
    else:
        return  status
