import numpy as np
import matplotlib.pyplot as plt

def eulerExplicito(func, t_interv, ini, n):
    def step(ti,h,func,ui):
        return ui+ h*func(ti,ui)
    
    t=np.linspace(t_interv[0], t_interv[1], n)
    h = t[1] - t[0]
    u = np.zeros((len(ini),n))
    u[:,0] = ini

    for i in range(0, n-1):
        u[:, i+1] = step(t[i],h,func,u[:,i])

    return u