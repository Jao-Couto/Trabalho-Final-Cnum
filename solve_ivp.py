import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.integrate._ivp.common import norm


def funcF(t, v):
    F = lambda x: 0.0039 + 0.0058/(1+np.exp(0.2*(x-35))) 
    normal = np.sqrt(v[0]**2+v[1]**2+v[2]**2)
    B = 4.1 * 10**-4
    w = 180*1.047198
    f0 = -F(normal)*normal*v[0]+B*w*(v[2]*np.sin(0)-v[1]*np.cos(0))
    f1 = -F(normal)*normal*v[1]+B*w*v[0]*np.cos(0)
    f2 = -F(normal)*normal*v[2]-B*w*v[0]*np.sin(0)-9.8

    return np.array([f0, f1, f2])

def funcU(t, u):
    s1 = u[0]*t
    s2 = u[1]*t
    s3 = u[2]*t
    return np.array([s1,s2,s3])

t_interval = [0, 3]    
t = np.linspace(t_interval[0], t_interval[1], 300) 

v0 = [38*np.cos(1), 0, 38*np.sin(1)]              
V = solve_ivp(funcF, t_interval, v0, t_eval=t).y  


s1 = []
s2 = []
s3 = []
aux = True
for i in range(0,300):
    s1.append((V[0,i])*(t[i]))
    s2.append((V[1,i])*(t[i]))
    s3.append((V[2,i])*(t[i]))

    if s3[-1] < 0:
        s3[-1] = 0
        if aux: 
            tempo_solve = t[i]
            print("\nTempo aproximado para atingir o chão com solve_ivp %f"%t[i])
        aux = False

plt.figure(4,figsize=(7,4), dpi=100)
plt.plot(t, s1, label='x')
plt.plot(t, s2, label='y')
plt.plot(t, s3, label='z')
plt.title('2, solve_ivp, h = %1.4f' % (t[1]-t[0]))
plt.legend()

