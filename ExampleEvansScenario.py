import numpy as np
from EvansA3Gurobi import *
import random
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
for _ in range(10000):
    p=[]
    #q=rand_constrained(3, 1)
    #q=[0.382198905698235, 0.5424588664225566, 0.07534222787920841] 0.85
    #q=[0.5923022271800285, 0.3931426966889069, 0.01455507613106466] 0.84
    #q=[0.4979045233418321, 0.03535180759722678, 0.4667436690609411]0.835
    #q=[0.5824135179560109, 0.39264706334818245, 0.024939418695806626]0.834
    #q=[0.49459710998726736, 0.47150929104017314, 0.0338935989725595] 0.834
    #q=[0.4935425216561825, 0.028197176115658085, 0.4782603022281594] #0.832
    q=[0.48,0.028,0.492]
    
    for b in range(2):
        for a in range(2):
            for x in range(3):
                if (b-a+f(a,x))%2==0:
                    p.append(q[x]/2)
                else:
                    p.append(0)

    p=np.array(p)
    I=[1/12 for _ in range(12)]
    I=np.array(I)
    v=0.832
    pv=v*p+(1-v)*I
    

    aux=EvansBehaviorCheckA3(pv)
    if aux=="non-classical":
        print(q)
        break

