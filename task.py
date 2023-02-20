import matplotlib.pyplot as plt
import numpy as nm
import sympy as sp

lim = 10
step=0.01
x=nm.arange(-lim,lim,step)

a,b,c,d,e = 2.0,17.0,-17.0,-8.0,6.0

def func(x):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e

# Корни уравнения
x = sp.symbols('x', real=True)
roots = sp.solveset(a*x**4 +b*x**3 +c*x**2 +d*x + e, x)
print(roots)
roots_list=list(roots)

# Вершина
x=nm.arange(-1*lim,lim,step)
min_y = min(func(x))
x = sp.symbols('x', real=True)
e1=e-min_y
min_x = sp.solveset(a*x**4 +b*x**3 +c*x**2 +d*x + e1, x)
min_xx=list(min_x)[0]
print(min_xx, min_y)

# Интервалы, на которых функция возрастает
x_down=nm.arange(-lim,min_xx,step)
x_up=nm.arange(min_xx,lim,step)

# Определить промежутки, на котором f > 0, f < 0
x_down_pos=nm.arange(-lim,roots_list[0],step)
x_down_neg=nm.arange(roots_list[0],min_xx,step)
x_up_neg=nm.arange(min_xx,roots_list[2],step)
x_up_pos=nm.arange(roots_list[2],lim,step)

plt.rcParams['lines.linestyle']='-'
plt.plot(x_down_pos,func(x_down_pos),'r',label='убывает, f>0')
plt.plot(x_up_pos,func(x_up_pos),'b',label='возрастает, f>0')
plt.rcParams['lines.linestyle']='-.'
plt.plot(x_down_neg,func(x_down_neg),'r',label='убывает, f<0')
plt.plot(x_up_neg,func(x_up_neg),'b',label='возрастает, f<0')
plt.plot(roots_list[0],0,'b.',label='Корни')
plt.plot(roots_list[1],0,'b.')
plt.plot(roots_list[2],0,'b.')
plt.plot(roots_list[2],0,'b.')
plt.plot(min_xx,min_y,'gx',label='Вершина')
plt.legend()
plt.grid()
plt.show()