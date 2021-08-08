import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.integrate._ivp.common import norm


def func(t, v):
    F = lambda x: 0.0039 + 0.0058/(1+np.exp(0.2*(x-35))) 
    normal = np.sqrt(v[0]**2+v[1]**2+v[2]**2)
    B = 4.1 * 10**-4
    w = 180*1.047198
    f0 = -F(normal)*normal*v[0]+B*w*(v[2]*np.sin(0)-v[1]*np.cos(0))
    f1 = -F(normal)*normal*v[1]+B*w*v[0]*np.cos(0)
    f2 = -F(normal)*normal*v[2]-B*w*v[0]*np.sin(0)-9.8

    return np.array([f0, f1, f2])

t_interval = [0, 0.5]                                    # Intervalo de t
conds = [38*np.cos(1), 0, 38*np.sin(1)]                  # Condição inicial (de u_1 e u_2 e u_3)
t = np.linspace(t_interval[0], t_interval[1], 51)        # definir as divisões (implica na escolha do h)
u = solve_ivp(func, t_interval, conds, t_eval=t).y       # A solução fica armazenada no atributo y do objeto de retorno, por isso ".y"

print(u[2][-10])
print(t[-10])
# Cada linha de u armazena a solução da equaçao respectiva
plt.figure(figsize=(7,4), dpi=100)
plt.plot(t, u[0], label='$u_1$ ')
plt.plot(t, u[1], label='$u_2$ ')
plt.plot(t, u[2], label='$u_3$ ')
plt.title('2, Solve_ivp, h = %f' % (t[1]-t[0]))
plt.legend()
plt.show()


#Atinge o chão depois de 2.5 segundos