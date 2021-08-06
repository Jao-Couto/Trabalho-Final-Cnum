import numpy as np
from numpy.core.arrayprint import printoptions
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def eulerExplicito(ydiff, y, z, x, u1, u2):
    print("Método de Euler explícito")
    n = len(x)
    Euler_ex = lambda y1, h, y_: y1 + h * y_
    yAprox = [y]
    zAprox = [z]
    h = x[1] - x[0]
    for i in range(0,n-1):
        y_n1 = Euler_ex(yAprox[-1],  h, ydiff[0](x[i], yAprox[-1], zAprox[-1]))
        z_n1 = Euler_ex(zAprox[-1],  h, ydiff[1](x[i], yAprox[-1], zAprox[-1]))
        erro1 = abs(u1(x[i])-y_n1)
        erro2 = abs(u1(x[i])-z_n1)
        print('%2d || u1 = %2.7f || u2 = %2.7f' % (i,erro1, erro2))
        yAprox.append(y_n1)
        zAprox.append(z_n1)
    
    print()
    plt.figure(1)
    plt.plot(x, yAprox, label='Esperado u1')
    plt.plot(x, u1(x), label='Aproximado explícito')
    plt.legend()
    plt.title("h = %f"% h)

    plt.figure(2)
    plt.plot(x, zAprox, label='Esperado u2')
    plt.plot(x, u2(x), label='Aproximado explícito')
    plt.legend()
    plt.title("h = %f"% h)


def eulerModificado(ydiff, y, z, t, u1, u2):
    print("Método de Euler modificado")
    n = len(t)
    yAprox = [y]
    zAprox = [z]
    h = t[1] - t[0]
    Euler_modificado = lambda y,k2, h: y + h*k2

    for i in range(0,n-1):
        k1 = ydiff[0](t[i],yAprox[-1], zAprox[-1])
        k2 = ydiff[0](t[i]+h/2, yAprox[-1]+h/2*k1, zAprox[-1]+h/2*k1)
        y_n1 = Euler_modificado(yAprox[-1], k2, h)

        k1 = ydiff[1](t[i],yAprox[-1], zAprox[-1])
        k2 = ydiff[1](t[i]+h/2, yAprox[-1]+h/2*k1, zAprox[-1]+h/2*k1)
        z_n1 = Euler_modificado(zAprox[-1], k2, h)
        erro1 = abs(u1(t[i])-y_n1)
        erro2 = abs(u2(t[i])-z_n1)
        print('%2d || u1 = %2.7f || u2 = %2.7f' % (i,erro1, erro2))
        yAprox.append(y_n1)
        zAprox.append(z_n1)
    
    print()
    plt.figure(1)
    plt.plot(t, yAprox, label='Aproximado Modificado')
    plt.legend()
    plt.title("u1, h = %f"% h)

    plt.figure(2)
    plt.plot(t, zAprox, label='Aproximado Modificado')
    plt.legend()
    plt.title("u2, h = %f"% h)

def eulerMelhorado(ydiff, y, z, t, u1, u2):
    print("Método de Euler melhorado")
    n = len(t)
    yAprox = [y]
    zAprox = [z]
    h = t[1] - t[0]
    Euler_melhorado = lambda y,k1,k2, h: y + (h/2)*(k1+k2)

    for i in range(0,n-1):
        k1 = ydiff[0](t[i],yAprox[-1], zAprox[-1])
        k2 = ydiff[0](t[i]+h, yAprox[-1]+h*k1, zAprox[-1]+h*k1)
        y_n1 = Euler_melhorado(yAprox[-1],k1, k2, h)

        k1 = ydiff[1](t[i],yAprox[-1], zAprox[-1])
        k2 = ydiff[1](t[i]+h, yAprox[-1]+h*k1, zAprox[-1]+h*k1)
        z_n1 = Euler_melhorado(zAprox[-1],k1, k2, h)

        erro1 = abs(u1(t[i])-y_n1)
        erro2 = abs(u2(t[i])-z_n1)
        print('%2d || u1 = %2.7f || u2 = %2.7f' % (i,erro1, erro2))
        yAprox.append(y_n1)
        zAprox.append(z_n1)
    
    print()
    plt.figure(1)
    plt.plot(t, yAprox, label='Aproximado Melhorado')
    plt.legend()
    plt.title("u1, h = %f"% h)

    plt.figure(2)
    plt.plot(t, zAprox, label='Aproximado Melhorado')
    plt.legend()
    plt.title("u2, h = %f"% h)


ydiff = [lambda t,y,z: 3*y +2*z -(2*(t**2)+1)*np.exp(2*t), lambda t,y,z: 4*y +z +(t**2 + 2*t -4)*np.exp(2*t)]
def func(t, u):
    u0 = u[1]*np.sin(t) + u[2]*np.cos(t)
    u1 = u[0]*np.sin(2*t) + u[2]*np.cos(2*t)
    u2 = u[0]*np.sin(3*t) + u[1]*np.cos(3*t)
    
t = np.linspace(0,1,6)
h = t[1] - t[0]
y = 1
z = 1

u1 = lambda t:(1/3)*np.exp(5*t)-(1/3)*np.exp(-t)+np.exp(2*t)
u2 = lambda t:(1/3)*np.exp(5*t)+(2/3)*np.exp(-t)+t**2*np.exp(2*t)

eulerExplicito(ydiff, y, z, t, u1, u2)
y = 1
z = 1
eulerModificado(ydiff, y, z, t, u1, u2)
y = 1
z = 1
eulerMelhorado(ydiff, y,z, t, u1, u2)

plt.show()