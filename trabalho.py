import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from EulerExplicito import eulerExplicito

def calcExata(uExata,t_interv, n):
    t=np.linspace(t_interv[0], t_interv[1], n)
    exata = []
    
    for i in range(0, len(uExata)):
        exataFun = []
        for j in range(0, len(t)):
            exataFun.append(uExata[i](t[j]))
        exata.append(exataFun)

    return exata

def calcErro(uAprox, uExata,t_interv, n):
    t=np.linspace(t_interv[0], t_interv[1], n)
    erro = []
    for i in range(0, len(uAprox)):
        nome = "u"+str(i)
        errofun = [nome]
        for j in range(0, len(t)):
            errofun.append(uExata[i](t[j])-uAprox[i,j])
        erro.append(errofun)
    return erro

def plot(uAprox, uExat, t_interv, n, tipo):
    t=np.linspace(t_interv[0], t_interv[1], n)
    h = t[1] -t[0]
    for i in range(0, len(uAprox)):
        plt.figure(i+1)
        plt.plot(t, uAprox[i], label='%s u%d'%(tipo,i+1))
        plt.plot(t, uExat[i], label='Esperado u%d'%(i+1))
        plt.legend()
        plt.title("h = %f"% h)



def func(t, u):
    u0 = 3*u[0] +2*u[1] -(2*(t**2)+1)*np.exp(2*t)
    u1 = 4*u[0] +u[1]+(t**2 + 2*t -4)*np.exp(2*t)
    return np.array([u0,u1])
    
inter = [0,1] 
un = [1,1]

u = eulerExplicito(func, inter, un, 6)

u1 = lambda t:(1/3)*np.exp(5*t)-(1/3)*np.exp(-t)+np.exp(2*t)
u2 = lambda t:(1/3)*np.exp(5*t)+(2/3)*np.exp(-t)+t**2*np.exp(2*t)

ex = [u1,u2]
erro = calcErro(u, ex, inter, 6)
print("\nErro Explícito:\n")
print(tabulate(erro,headers=["1","2","3","4","5","6"]))

exata = calcExata(ex,inter,6)
plot(u, exata, inter, 6, "Explícito")
plt.show()