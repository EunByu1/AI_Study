def factorial(x):
  """
  factorial function
  input  : 정수 x
  output : x!
  """
  x_list = list(range(1, x+1))
  res    = 1
  for val in x_list:
    res *= val
  return res 


# ================== count 10 ==================
n = 10
e = 0

for i in range(0,n):
    e += 1/factorial(i)

print(f"euler number(count 10): {e}")
# ==============================================


# ================== count 100 ==================
n = 10
e = 0

for i in range(0,n):
    e += 1/factorial(i)

print(f"euler number(count 10): {e}")
# ==============================================
