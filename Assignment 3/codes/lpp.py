
import numpy as np
import pulp as p
Lp_prob = p.LpProblem('Minimize', p.LpMinimize)  

  
# Create problem Variables  
x = p.LpVariable("x", lowBound = 0)    
y = p.LpVariable("y", lowBound = 0)   
   
Lp_prob +=  x + 2 * y    
  
# Constraints: 
Lp_prob += x + 2 * y >= 100
Lp_prob += 2*x - y <= 100
Lp_prob += 2*x +y >= 200
Lp_prob += x >= 0
Lp_prob += y >= 0
  
# Display the problem 
#print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
  
print("Minimum = ", p.value(Lp_prob.objective))

Lp_prob = p.LpProblem('Maximize', p.LpMaximize)

x = p.LpVariable("x", lowBound = 0)    
y = p.LpVariable("y", lowBound = 0)   
   
Lp_prob +=  x + 2 * y    
  
# Constraints: 
Lp_prob += x + 2 * y >= 100
Lp_prob += 2*x - y <= 100
Lp_prob += 2*x +y >= 200
Lp_prob += x >= 0
Lp_prob += y >= 0 
  
status = Lp_prob.solve()   # Solver 
   
print("Maximum = ", p.value(Lp_prob.objective))

import matplotlib.pyplot as plt
%matplotlib inline

# Construct lines
x = np.array([0, 20, 200])
y1 = []
y2 = []
y3 = []
for i in range(3):
  y1.append((100-x[i])/2.0)  # x + 2y >= 100
  
  y2.append(2*x[i])     # 2X - y <= 0 
  
  y3.append(200 - 2 * x[i])     # 2x + y <=200



# Make plot
plt.plot(x, y1, label=r'$y\geq(100-x)/2$')
plt.plot(x, y2, label=r'$y\geq2x$')
plt.plot(x, y3, label=r'$y\leq 200-2x $')

plt.xlim((0, 150))
plt.ylim((0, 300))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
