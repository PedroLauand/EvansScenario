import numpy as np
from EvansA3Gurobi import *
from NLEvans import *
import random
import Indices as ind  
def f(a,x):
    if x==0:
        return 0
    elif x==1:
        return a
    elif x==2:
        return (a+1)%2

def rand_constrained(n, total):
    # l is a sorted list of n-1 random numbers between 0 and total
    l = sorted([0] + [total * random.random() for i in range(n - 1)] + [total])
    # Return the intervals between each successive element
    return [l[i + 1] - l[i] for i in range(n)]
L=[]
l=[]
while len(L)<=10000:
    p=rand_constrained(12, 1)
    p=np.array(p)
 
    aux=NLEvans(p)
    print(aux)
    if aux<0.99:
        L.append(p)
        l.append(aux)
        np.savetxt("EvanspointsX3.txt",L)
        np.savetxt("NLEvans.txt",l)

        print(len(L),len(l))
    
