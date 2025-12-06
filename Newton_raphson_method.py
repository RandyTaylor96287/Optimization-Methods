import math
# ToDo: Uncomment the line below ("import ...") once you have implemented plot_iterations.
# You may need to install Matplotlib first: pip install matplotlib
import matplotlib.pyplot as plt 

# ============================================
# get_polynomial_value:
# ============================================

# ToDo: Write the get_polynomial_value function

# Uncomment the line below and implement the function:
def get_polynomial_value(x, polynomial_coefficients):  
  polynomial_value = 0                                      # initialize polynomial_value
  for exponent in range(len(polynomial_coefficients)):      # assume the order of arguments goes up from left to right side
    polynomial_value += polynomial_coefficients[exponent] * (x ** exponent)
  return polynomial_value

# ============================================
# differentiate_polynomial:
# ============================================

# ToDo: Write the differentiate_polynomial function

# Uncomment the line below and implement the function:
def differentiate_polynomial(polynomial_coefficients, derivative_order):
  
  copy_coefficients = polynomial_coefficients.copy()       # avoid damaging original data

  if derivative_order == 0:
    return polynomial_coefficients.copy()                  # case when derivative_order is 0

  for exponent in range(derivative_order):                 # case when derivative_order >= len(polynomial_coefficients)
    if derivative_order >= len(polynomial_coefficients):
      print('The degree of the polynomial must be 2 or larger')
      return [0]

    temp_coefficients = []
    for exponent in range(1, len(copy_coefficients)):
      temp_coefficients.append(copy_coefficients[exponent] * exponent)

    copy_coefficients = temp_coefficients
  return copy_coefficients
  

# ============================================
# step_newton_raphson:
# ============================================

# ToDo: Write the step_newton_raphson function

# Uncomment the line below and implement the function:
def step_newton_raphson(x, f_prime, f_double_prime):
  x_new = 0
 
  x_new = x - f_prime / f_double_prime
  return x_new

# ============================================
# run_newton-raphson:
# ============================================
     
# ToDo: Write the run_newton-raphson function

# Uncomment the line below and implement the function:
def run_newton_raphson(polynomial_coefficients, starting_point, tolerance, maximum_number_of_iterations):
  prime_coefficient = differentiate_polynomial(polynomial_coefficients, 1)
  double_prime_coefficient = differentiate_polynomial(polynomial_coefficients, 2)
  x = starting_point
  converged = False
  iteration_steps = 0
  final_gradient = 0
  
  iterations = {'x_values': [x], 'f_values': [get_polynomial_value(x, polynomial_coefficients)]}

  for steps in range(maximum_number_of_iterations):
    f_prime = get_polynomial_value(x, prime_coefficient)
    f_double_prime = get_polynomial_value(x, double_prime_coefficient)

    if (f_double_prime == 0):
      print('Unappliable value of second-derivative')
      break

    x = step_newton_raphson(x, f_prime, f_double_prime)

    iterations['x_values'].append(x)
    iterations['f_values'].append(get_polynomial_value(x, polynomial_coefficients))

    if abs(iterations['x_values'][iteration_steps + 1] - iterations['x_values'][iteration_steps]) < tolerance:
      converged = True
      final_gradient = f_prime
      iteration_steps = steps + 1
      break

    iteration_steps = steps + 1
    final_gradient = f_prime

  print('Final gradient:', f_prime, 'Iteration steps:', iteration_steps, 'Minimum Point', x, 'Converged?', converged)

  return iterations
    

# ============================================
# plot_iterations:
# ============================================

# ToDo: Write the plot_iterations function
#
# Here, you should use matplotlib. 
# Note: You must uncomment the second "import ..." statement above
# Then uncomment the line below and implement the function:
def plot_iterations(polynomial_coefficients,iterations):
  plt.figure(figsize=(12, 8))
    
  x_min = min(iterations['x_values']) - 1
  x_max = max(iterations['x_values']) + 1
    
  num_points = 200
  step = (x_max - x_min) / (num_points - 1)
  x_values = [x_min + i * step for i in range(num_points)]
    
  y_values = []
  for x in x_values:
    y_values.append(get_polynomial_value(x, polynomial_coefficients))
    
  plt.plot(x_values, y_values, 'b-', linewidth=2)
    
  x_vals = iterations['x_values']
  f_vals = iterations['f_values']
    
  for i in range(len(x_vals) - 1):
    plt.plot([x_vals[i], x_vals[i+1]], [f_vals[i], f_vals[i+1]], 'r--', alpha=0.7)
    
  plt.plot(x_vals[0], f_vals[0], 'go', markersize=10, label='Start point')
  plt.plot(x_vals[-1], f_vals[-1], 'mo', markersize=10, label='Final point')
    
  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.title('Newton-Raphson Iteration Process')
  plt.legend()
  plt.grid(True, alpha=0.3)
    
  plt.show()


# ============================================
# Main loop
# ============================================

tolerance = 0.00001
maximum_number_of_iterations = 100

polynomial_coefficients = [5]
starting_point = 6

# ToDo: Uncomment the two lines below, once you have implemented the functions above:
iterations = run_newton_raphson(polynomial_coefficients, starting_point, tolerance, maximum_number_of_iterations)
plot_iterations(polynomial_coefficients, iterations)