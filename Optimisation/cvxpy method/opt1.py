import numpy as np
from cvxpy import *


#function parameters
P = np.array([4,6.28])    
V = np.array([[1,0],[0,3.14]])
u = np.array([0,0]).reshape(2,-1)

x = Variable((2,1))

#function
f =  quad_form(x,V)
obj = Minimize(f)

#Constraints

constraints = [P@x-28 == 0]
#solution
Problem(obj, constraints).solve()

print((f.value),x.value)
