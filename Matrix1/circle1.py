import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
I=np.eye(2)
e1=I[:,0]

def circ_gen(O,r):
   len = 50
   theta = np.linspace(0,2*np.pi,len)
   x_circ = np.zeros((2,len))
   x_circ[0,:] = r*np.cos(theta)
   x_circ[1,:] = r*np.sin(theta)
   x_circ = (x_circ.T + O).T
   return x_circ
def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB
#i\p
theta =120*np.pi/180
theta1=30*np.pi/180
theta2=60*np.pi/180
O=np.array(([0,0]))
r=3
A=np.array(([r*np.cos(theta1),r*np.sin(theta1)]))
B=np.array(([r*np.cos(theta-theta1),-r*np.sin(theta-theta1)]))
C=np.array(([-r*np.cos(theta2),r*np.sin(theta2)]))
D=np.array(([-r*np.cos(theta-theta2),-r*np.sin(theta-theta2)]))
M1=(A+B)/2
M2=(C+D)/2
r2=np.linalg.norm(M1)



#circle
x_circ=circ_gen(O,r)
x_circ1=circ_gen(O,r2)

#circleplot
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circles$')
tri_coords = np.vstack((A,B,O,C,D,M1,M2)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','O','C','D','M1','M2']
plt.plot(x_circ1[0,:],x_circ1[1,:],'r--',label='$Circles$')

for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#li
x_AB = line_gen(A,B)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OM1 = line_gen(O,M1)
x_OM2=line_gen(O,M2)
#x_BC = line_gen(B,C)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)
#x_BC = line_gen(B,C)
x_CD = line_gen(C,D)


#liplot
plt.plot(x_OA[0,:],x_OA[1,:])
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_OB[0,:],x_OB[1,:])
plt.plot(x_OM1[0,:],x_OM1[1,:])
plt.plot(x_OM2[0,:],x_OM2[1,:])
plt.plot(x_OC[0,:],x_OC[1,:])
plt.plot(x_OD[0,:],x_OD[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])

#plt.plot(x_BC[0,:],x_BC[1,:])

plt.show()