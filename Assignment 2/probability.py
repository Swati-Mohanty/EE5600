import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
import random

sample_size= 36
total = 0
#for i in range(sample_size):
   # if ((6,5) or (5,6)) in [(randint(1,6), randint(1,6)) ]:
      #  total +=1
#print("The probability two 6 turns up when rolling 2 die 36 times is:",total)


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


# Driver Code
num = 3
start = 1
end = 6
a=0
b =0
ss =[[]]
for i in range(216):
    ss =[(Rand(start, end, num))]
    #print (ss)
    if (ss[0][2]==4):
        a+=1
        print(ss)
    if((ss[0][0]==6)&(ss[0][1]==5)):
        b+=1

p_a = float(a)/216
p_b = float(b)/216
print (p_a)
print (p_b)
p_r = (p_a * p_b)/p_b
print (p_r)
print("Simulation probability = ",p_r)
print ("Theoretical probability = ",0.167)
error = abs(0.167-p_r)/p_r
print("Simulation error %:", error*100 )

