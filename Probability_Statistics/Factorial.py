def factorial(x):
  """
  factorial function
  input : 정수 x
  output: x!
  """
  x_list = list(range(1, x+1))
  res    = 1
  for val in x_list:
    res *= val
  return res 

x = int(input())
print(f"factorial {x}: {factorial(x)}")
