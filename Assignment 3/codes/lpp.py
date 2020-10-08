
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
