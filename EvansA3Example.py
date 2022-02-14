from EvansA3Gurobi import *
import numpy as np
from Indices import *
import random
'''I=[1/16 for _ in range(16)]
I=np.array(I)
print(EvansBehaviorCheckA4(I))
p=np.zeros(16)
p[evansObIndexA4(0,0,0)]=1/2
p[evansObIndexA4(1,0,1)]=1/2
v=0.35
pv=v*p+(1-v)*I'''
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
'''for _ in range(100):
    pQ=np.random.uniform(low=0,high=1,size=16)
    pQ=(1/np.sum(pQ))*pQ
    print(pQ)
    aux=EvansBehaviorCheckA4(pQ)
    if aux=="non-classical":
        print(aux)
        break'''

'''ket0=np.array([1,0])
ket1=np.array([0,1])
sig0=np.array([[0,1],[1,0]])
sig1=np.array([[0,-1j],[1j,0]])
sig2=np.array([[1,0],[0,-1]])

S0=[0.5*(np.eye(2)+sig0),0.5*(np.eye(2)-sig0)]
S1=[0.5*(np.eye(2)+sig1),0.5*(np.eye(2)-sig1)]
S2=[0.5*(np.eye(2)+sig2),0.5*(np.eye(2)-sig2)]

S_plus=[0.5*(np.eye(2)+1/np.sqrt(2)*(sig0+sig2)),0.5*(np.eye(2)-1/np.sqrt(2)*(sig0+sig2))]
S_minus=[0.5*(np.eye(2)+1/np.sqrt(2)*(sig2-sig0)),0.5*(np.eye(2)-1/np.sqrt(2)*(sig2-sig0))]
S=[S_plus[1],S_plus[0]]

phi_plus=1/np.sqrt(2)*(np.kron(ket0,ket0)+np.kron(ket1,ket1))
phi_minus=1/np.sqrt(2)*(np.kron(ket0,ket0)-np.kron(ket1,ket1))

phi1_plus=1/np.sqrt(2)*(np.kron(ket1,ket0)+np.kron(ket0,ket1))
phi1_minus=1/np.sqrt(2)*(np.kron(ket0,ket1)-np.kron(ket1,ket0))

h=1/2*np.kron(ket0,ket0)+np.sqrt(3)/2*np.kron(ket1,ket1)
psi=np.outer(h,h)
state=np.outer(phi_plus,phi_plus.conj()) 
state1=np.outer(phi_minus,phi_minus.conj()) 
state2=np.outer(phi1_plus,phi1_plus.conj()) 

state3=np.outer(phi1_minus,phi1_minus.conj()) 
q=[0.3,0.5,0.2]
pQ=pQ_Inst(psi,S0,S2,S,S_plus,S_minus,q)
v=1
pQ=v*pQ+(1-v)*I
print(pQ)
print(EvansBehaviorCheckA3(pQ))'''

