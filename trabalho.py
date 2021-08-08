import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from EulerExplicito import eulerExplicito
from EulerMelhorado import eulerMelhorado
from EulerModificado import eulerModificado


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

def plot(uAproxExp, uAproxMod, uAproxMel, uExat, t_interv, n, exerc):
    t=np.linspace(t_interv[0], t_interv[1], n)
    h = t[1] -t[0]
    for i in range(len(uExat)):
        plt.figure(i+1)
        plt.plot(t, uExat[i], label="Exata")
    nomeTipos = ["Explícita", "Modificada", "Melhorada"]
    aproximaList = [uAproxExp, uAproxMod, uAproxMel]

    for uAprox, tipo in zip(aproximaList, nomeTipos):
        for i in range(len(uAprox)):
            plt.figure(i+1)
            plt.plot(t, uAprox[i], label='%s u%d'%(tipo,i+1))
            plt.legend()
            plt.title("%s, h = %f"% (exerc, h))
    

#-----------------------------------------------EXERCÍCIO 1-----------------------------------------------------
#A)
def funcA(t, u):
    u0 = 3*u[0] +2*u[1] -(2*(t**2)+1)*np.exp(2*t)
    u1 = 4*u[0] +u[1]+(t**2 + 2*t -4)*np.exp(2*t)
    return np.array([u0,u1])
    
inter = [0,1] 
un = [1,1]

uExp = eulerExplicito(funcA, inter, un, 6)
uMel = eulerMelhorado(funcA, inter, un, 6)
uMod = eulerModificado(funcA, inter, un, 6)

u1 = lambda t:(1/3)*np.exp(5*t)-(1/3)*np.exp(-t)+np.exp(2*t)
u2 = lambda t:(1/3)*np.exp(5*t)+(2/3)*np.exp(-t)+t**2*np.exp(2*t)
N = 6

ex = [u1,u2]
header = [str(x) for x in range(1, N+1)]
erroExp = calcErro(uExp, ex, inter, N)
print("\nErro Explícito:\n")
print(tabulate(erroExp,headers=header))

erroMel = calcErro(uMel, ex, inter, N)
print("\nErro Melhorada:\n")
print(tabulate(erroMel,headers=header))

erroMod = calcErro(uMod, ex, inter, N)
print("\nErro Modificada:\n")
print(tabulate(erroMod,headers=header))

exata = calcExata(ex,inter,N)
plot(uExp, uMel, uMod, exata, inter, N, "1a")
plt.show()


#B)
def funcB(t, u):
    u0 = -4*u[0] - 2*u[1] + np.cos(t) + 4*np.sin(t)
    u1 = 3*u[0] + u[1] - 3*np.sin(t)
    return np.array([u0,u1])
    
inter = [0,2] 
un = [0,-1]
N = 21

uExp = eulerExplicito(funcB, inter, un, N)
uMel = eulerMelhorado(funcB, inter, un, N)
uMod = eulerModificado(funcB, inter, un, N)

u1 = lambda t:  2*np.exp(-t) - 2*np.exp(-2*t) + np.sin(t)
u2 = lambda t: -3*np.exp(-t) + 2*np.exp(-2*t)

ex = [u1,u2]
header = [str(x) for x in range(1, N+1)]
erroExp = calcErro(uExp, ex, inter, N)
print("\nErro Explícito:\n")
print(tabulate(erroExp,headers=header))

erroMel = calcErro(uMel, ex, inter, N)
print("\nErro Melhorada:\n")
print(tabulate(erroMel,headers=header))

erroMod = calcErro(uMod, ex, inter, N)
print("\nErro Modificada:\n")
print(tabulate(erroMod,headers=header))

exata = calcExata(ex,inter,N)
plot(uExp, uMel, uMod, exata, inter, N, "1b")
plt.show()

#C)
def funcC(t, u):
    u0 = u[1]
    u1 = -u[0] - 2*np.exp(t) + 1
    u2 = -u[0] - np.exp(t) + 1
    return np.array([u0,u1, u2])
    
inter = [0,2] 
un = [1, 0, 1]
N = 5

uExp = eulerExplicito(funcC, inter, un, N)
uMel = eulerMelhorado(funcC, inter, un, N)
uMod = eulerModificado(funcC, inter, un, N)

u1 = lambda t: np.cos(t) + np.sin(t) - np.exp(t) + 1
u2 = lambda t: np.cos(t) - np.sin(t) - np.exp(t)
u3 = lambda t: np.cos(t) - np.sin(t)

ex = [u1,u2, u3]
header = [str(x) for x in range(1, N+1)]
erroExp = calcErro(uExp, ex, inter, N)
print("\nErro Explícito:\n")
print(tabulate(erroExp,headers=header))

erroMel = calcErro(uMel, ex, inter, N)
print("\nErro Melhorada:\n")
print(tabulate(erroMel,headers=header))

erroMod = calcErro(uMod, ex, inter, N)
print("\nErro Modificada:\n")
print(tabulate(erroMod,headers=header))

exata = calcExata(ex,inter,N)
plot(uExp, uMel, uMod, exata, inter, N, "1c")
plt.show()


#D)
def funcD(t, u):
    u0 = u[1] - u[2] + t
    u1 = 3 * t**2
    u2 = u[1] + np.exp(-t)
    return np.array([u0,u1, u2])
    
inter = [0,1] 
un = [1, 1, -1]
N = 11

uExp = eulerExplicito(funcD, inter, un, N)
uMel = eulerMelhorado(funcD, inter, un, N)
uMod = eulerModificado(funcD, inter, un, N)

u1 = lambda t: -0.05*t**5 + 0.25*t**4 + t + 2 - np.exp(-t)
u2 = lambda t: t**3 + 1
u3 = lambda t: 0.25*t**4 + t - np.exp(-t)

ex = [u1,u2, u3]
header = [str(x) for x in range(1, N)]
erroExp = calcErro(uExp, ex, inter, N)
print("\nErro Explícito:\n")
print(tabulate(erroExp,headers=header))

erroMel = calcErro(uMel, ex, inter, N)
print("\nErro Melhorada:\n")
print(tabulate(erroMel,headers=header))

erroMod = calcErro(uMod, ex, inter, N)
print("\nErro Modificada:\n")
print(tabulate(erroMod,headers=header))

exata = calcExata(ex,inter,N)
plot(uExp, uMel, uMod, exata, inter, N, "1d")
plt.show()



#2
def func2(t, v):
    F = lambda x: 0.0039 + 0.0058/(1+np.exp(0.2*(x-35))) 
    normal = np.sqrt(v[0]**2+v[1]**2+v[2]**2)
    B = 4.1 * 10**-4
    w = 180*1.047198
    f0 = -F(normal)*normal*v[0]+B*w*(v[2]*np.sin(0)-v[1]*np.cos(0))
    f1 = -F(normal)*normal*v[1]+B*w*v[0]*np.cos(0)
    f2 = -F(normal)*normal*v[2]-B*w*v[0]*np.sin(0)-9.8

    return np.array([f0, f1, f2])

inter = [0,0.5] 
un = [38*np.cos(1), 0, 38*np.sin(1)] 
N = 51

uExp = eulerExplicito(func2, inter, un, N)
uMel = eulerMelhorado(func2, inter, un, N)
uMod = eulerModificado(func2, inter, un, N)

exata = calcExata(ex,inter,N)
plot(uExp, uMel, uMod, exata, inter, N, "2")
plt.show()

import solve_ivp
#Atinge o chão depois de 2.5 segundos