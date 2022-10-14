#Python libraries for math and graphics

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
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

I=np.eye(2)
e1=I[:,0]

#circle parameters
r=3
k=1.5
O=np.array(([0,0]))
#M=np.array(([1.366,0.366]))
theta =120*np.pi/180
theta1=30*np.pi/180
O=np.array(([0,0]))
r=3
A=np.array(([r*np.cos(theta1),r*np.sin(theta1)]))
B=np.array(([r*np.cos(theta-theta1),-r*np.sin(theta-theta1)]))
M=(A+B)/2
print(M)
#Generating the line
m=-e1
k1=-10
k2=10
xAB=line_gen(A,B)
xOA=line_gen(O,A)
xOB=line_gen(O,B)
xOM=line_gen(O,M)

#Generating the circle 
x_circ1=circ_gen(O,r)
x_circ2=circ_gen(O,k)
#plotting all the lines
plt.plot(xAB[0,:],xAB[1,:],label='Chord')
plt.plot(xOB[0,:],xOB[1,:],label='radius')
plt.plot(xOA[0,:],xOA[1,:],label='radius')
plt.plot(xOM[0,:],xOM[1,:],label='chord bisector')
#plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='Circle')
plt.plot(x_circ2[0,:],x_circ2[1,:],'r--',label='locus')

#locus of midpoint of chord of the circle which subtends a right angle at the origin
#here locus is nothing but equation of the the points (x,y) and (0,0) which forms  a perpenducluar 
#from the figure

#labeling the coordinates
tri_coords = np.vstack((O,A,B,M)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O(0,0)','A(1,1.732)','B(1.732,-1)','M(x,y)']
for i, txt in enumerate(vert_labels):
	plt.annotate(txt, # this is the text
        (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
        textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
   
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show() 
#plt.savefig('/sdcard/Download/c2_fwc/trunk/circle_assignment/docs/circle.png')
#subprocess.run(shlex.split("termux-open '/sdcard/Download/c2_fwc/trunk/circle_assignment/docs/main.pdf' "))
