import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
import math

def form_eqn(n,d):
    a = -2*n[0]
    b = -2*n[1]
    s = d*d + (a+b)
    print("Equation of circle is : (x^2 + y^2  ",a,"x ",b,"y =", s)


c = np.array([2,2])
p = np.array([4,5])
r = math.sqrt(math.pow((p[0]-c[0]),2)+math.pow((p[1]-c[1]),2))
form_eqn(c,r)
