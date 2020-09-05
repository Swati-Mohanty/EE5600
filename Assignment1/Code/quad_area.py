import numpy as np


#Line points
A = np.array([-1,0.5,4])
B = np.array([1,0.5,4])
C = np.array([1,-0.5,4])
D = np.array([-1,-0.5,4])

#adjacent sides
AD = np.linalg.norm(A-D)
BA = np.linalg.norm(B-A)

#Area= cross product of adjacent sides
area = AD*BA
print("Area of rectangle=",area)
