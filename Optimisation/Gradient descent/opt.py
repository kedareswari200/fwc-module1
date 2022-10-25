import numpy as np
import matplotlib.pyplot as plt
#import cvxpy  as cp

import sys, os
sys.path.insert(0,'/home/Desktop/Matricx/CoordGeo')

#if using termux
import subprocess
import shlex
r = 28
a = 28 -r
def f(x):
 return (x**2)/16 + ((28-4*x)**2/12.56) 
label_str = "$9x^2 + 12x +2$"

#For minima using gradient descent
cur_x = -1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: (x/8)-((28-4*x)/0.636)             

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x)
print("Minimum value of line f(x) is ", min_val, "at","x =",cur_x)
print("Minimum value for circle is",28 - cur_x)
#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
#plt.savefig('/sdcard/Linearalgebra/opt2.pdf')
#plt.show()
