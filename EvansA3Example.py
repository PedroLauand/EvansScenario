from EvansA3Gurobi import *
import numpy as np
from Indices import *
import random
def rand_constrained(n, total):
    # l is a sorted list of n-1 random numbers between 0 and total
    l = sorted([0] + [total * random.random() for i in range(n - 1)] + [total])
    # Return the intervals between each successive element
    return [l[i + 1] - l[i] for i in range(n)]
for _ in range(1000):
     
    q_x=rand_constrained(4, 1)
    
    pQ=np.zeros(16)
    pQ[evansObIndexA4(0,0,0)]=q_x[0]*0.426777
    pQ[evansObIndexA4(0,0,1)]=q_x[0]*0.0732233
    pQ[evansObIndexA4(0,1,0)]=q_x[0]*0.426777
    pQ[evansObIndexA4(0,1,1)]=q_x[0]*0.0732233

    pQ[evansObIndexA4(1,0,0)]=q_x[1]*0.426777
    pQ[evansObIndexA4(1,0,1)]=q_x[1]*0.0732233
    pQ[evansObIndexA4(1,1,0)]=q_x[1]*0.0732233
    pQ[evansObIndexA4(1,1,1)]=q_x[1]*0.426777


    pQ[evansObIndexA4(2,0,0)]=q_x[2]*0.0732233
    pQ[evansObIndexA4(2,0,1)]=q_x[2]*0.426777
    pQ[evansObIndexA4(2,1,0)]=q_x[2]*0.0732233
    pQ[evansObIndexA4(2,1,1)]=q_x[2]*0.426777


    pQ[evansObIndexA4(3,0,0)]=q_x[3]*0.0732233
    pQ[evansObIndexA4(3,0,1)]=q_x[3]*0.426777
    pQ[evansObIndexA4(3,1,0)]=q_x[3]*0.426777
    pQ[evansObIndexA4(3,1,1)]=q_x[3]*0.0732233


    I=[1/16 for _ in range(16)]
    I=np.array(I)
    v=1
    pQ=v*pQ+(1-v)*I

    aux=EvansBehaviorCheckA4(pQ)
    print(aux)
    if aux=="non-classical":
        print(q_x)


