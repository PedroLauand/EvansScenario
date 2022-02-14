def PEvans(state1,state2,A0,A1,B,C0,C1):
#Construimos um comportamento do Cenario de Evans dado uma realização quantica. 
#A0,A1,B,C0,C1 devem ser listas de matrizes com os efeitos quanticos. Os stados tambem devem ser matrizes.
    import numpy as np
    p=[]
    rho=np.kron(state1,state2)
    for c in range(2):
        for b in range(2):
            for a in range(3):
                if b==0:
                    p=np.append(p,np.trace(rho@(np.kron(A0[a],np.kron(B[0],C0[c])))))
                elif b==1:
                    p=np.append(p,np.trace(rho@(np.kron(A1[a],np.kron(B[1],C1[c])))))

    p=np.real(p)
    return p
import numpy as np
import EvansA3Gurobi as bl
M0=np.array([[0.84153, -0.15627],[-0.15627 ,0.02902]])
M1=np.array([[0.14061, 0.25242],[0.25242, 0.45314]])
M2=np.eye(2)-M0-M1
#print(np.all(np.linalg.eigvals(M0) >= 0))
#print(np.all(np.linalg.eigvals(M1) >= 0))
#print(np.all(np.linalg.eigvals(M2) >= 0))
A0=[M0,M1,M2]
ket0=np.array([1,0])
ket1=np.array([0,1])
plus=np.array([1/np.sqrt(2),1/np.sqrt(2)])
q=0.5857
E0=q*np.outer(ket0,ket0)
E1=q*(np.outer(plus,plus))
E2=np.eye(2)-E0-E1

A1=[E0,E1,E2]
phi_plus=1/np.sqrt(2)*(np.kron(ket0,ket0)+np.kron(ket1,ket1))
phi_minus=1/np.sqrt(2)*(np.kron(ket0,ket0)-np.kron(ket1,ket1))

phi1_plus=1/np.sqrt(2)*(np.kron(ket1,ket0)+np.kron(ket0,ket1))
phi1_minus=1/np.sqrt(2)*(np.kron(ket1,ket0)-np.kron(ket0,ket1))


state=np.outer(phi_plus,phi_plus.conj()) 
state1=np.outer(phi_minus,phi_minus.conj()) 

state2=np.outer(phi1_plus,phi1_plus.conj()) 
state3=np.outer(phi1_minus,phi1_minus.conj()) 
B0=state+state1
B1=state2+state3

B=[B0,B1]

sig0=np.array([[0,1],[1,0]])
sig1=np.array([[0,-1j],[1j,0]])
sig2=np.array([[1,0],[0,-1]])

#C0=[0.5*(np.eye(2)+sig0),0.5*(np.eye(2)-sig0)]
#C0=[0.5*(np.eye(2)+sig1),0.5*(np.eye(2)-sig1)]
#C1=[0.5*(np.eye(2)+sig2),0.5*(np.eye(2)-sig2)]
C0=[0.5*(np.eye(2)+1/np.sqrt(2)*(sig0+sig2)),0.5*(np.eye(2)-1/np.sqrt(2)*(sig0+sig2))]
#C1=[0.5*(np.eye(2)+sig1),0.5*(np.eye(2)-sig1)]
C1=[0.5*(np.eye(2)+1/np.sqrt(2)*(sig0-sig2)),0.5*(np.eye(2)-1/np.sqrt(2)*(sig0-sig2))]

p=PEvans(state,state2,A0,A1,B,C0,C1)

print(bl.EvansBehaviorCheckA3(p))