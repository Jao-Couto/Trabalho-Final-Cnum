import numpy as np
import matplotlib.pyplot as plt

def eulerModificado(func, t_interv, ini, n):
    def step(h,ui, k2):
        return ui + h *k2
    

    t=np.linspace(t_interv[0], t_interv[1], n)
    h = t[1] - t[0]
    u = np.zeros((len(ini),n))
    u[:,0] = ini

    for i in range(0,n-1):
        k1 = func(t[i],u[:, i])
        k2 = func(t[i]+(h/2), u[:, i]+(h/2)*k1)
        u[:, i+1] = step(h, u[:, i], k2)
    
    return u     

