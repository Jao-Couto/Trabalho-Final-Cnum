import numpy as np
import matplotlib.pyplot as plt

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