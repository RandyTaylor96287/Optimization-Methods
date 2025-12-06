import math
import numpy as np # optional - uncomment and use if you wish

# ==============================
# run_gradient_descent function:
# ==============================

# To do: Write this function (uncomment the line below).
def run_gradient_descent(x_start, mu, eta, gradient_tolerance):

  MAXITERATION = 1000000
  x_1 = x_start[0]
  x_2 = x_start[1]           
  converged = False                   # initialization

  for i in range(MAXITERATION):
    
    x_temp = [x_1,x_2]
    gradient = compute_gradient(x_temp,mu)
    gradient_x1 = gradient[0]
    gradient_x2 = gradient[1]

    x_1 -= eta * gradient_x1     # gradient descend
    x_2 -= eta * gradient_x2

    gradient = [gradient_x1,gradient_x2]
    norm = np.linalg.norm(gradient)   # L2 norm

    if norm < gradient_tolerance:
      print(f'f is converged after {i+1} times of iterations')
      converged = True
      break
  if not converged:
    print('Did not converge within the maximum iterations')
  return x_temp

# ==============================
# compute_gradient function:
# ==============================

# To do: Write this function (uncomment the line below).
def compute_gradient(x, mu):

  x_1 = x[0]
  x_2 = x[1]

  constraint_value = x_1**2 + x_2**2 - 1
    
  if constraint_value > 0:          # categorization 
    gradient_x1 = 2*(x_1 - 1) + 4*mu*x_1*constraint_value
    gradient_x2 = 4*(x_2 - 2) + 4*mu*x_2*constraint_value
  else:  
    gradient_x1 = 2*(x_1 - 1)
    gradient_x2 = 4*(x_2 - 2)

  gradient = [gradient_x1,gradient_x2]

  return gradient

# ==============================
# Main program:
# ==============================

x_start = [1,2]
mu_values = [1, 10, 100,1000]
eta = 0.0001
# x_start = ... add a two-component vector here, with the chosen starting point
gradient_tolerance = 0.0000001

for mu in mu_values:
  x = run_gradient_descent(x_start, mu, eta, gradient_tolerance)
  output = f"x = ({x[0]:.4f}, {x[1]:.4f}), mu = {mu:.1f}"
  print(output)


