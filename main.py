# main.py
import cvxpy as cp

# Define Variables
XB = cp.Variable(nonneg=True)
XC = cp.Variable(nonneg=True)

# Define Objective Function
profit = 25 * XB + 30 * XC

# Define Constraints
constraints = [
    (1/200) * XB + (1/140) * XC <= 40,  # Time
    XB <= 6000, # XB Upper Limit    
    XC <= 4000  # XC Upper Limit
]

# Define Optimization Problem
problem = cp.Problem(cp.Maximize(profit), constraints)

# Solve
problem.solve()

print(f"XB = {XB.value}")
print(f"XC = {XC.value}")
print(f"Maximum Profit = {problem.value}")