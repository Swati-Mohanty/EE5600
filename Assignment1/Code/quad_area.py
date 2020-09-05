
import numpy as np


#Line points
A = np.array([-1,0.5,4])
B = np.array([1,0.5,4])
C = np.array([1,-0.5,4])
D = np.array([-1,-0.5,4])

#adjacent sides
AD = np.linalg.norm(A-D)
BA = np.linalg.norm(B-A)

#Area= product of adjacent sides
area = AD*BA
print("Area of rectangle=",area)

#Cross product
ar = np.linalg.norm(np.cross(A-D,B-A))
print("Cross product area=",ar)
