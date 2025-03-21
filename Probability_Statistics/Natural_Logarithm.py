# ================== Method 1 ==================
def log(x):
  """
  natural logarithm function
  input  : argument of the logarithm
  output : ln(x)
  """
  n   = 100000000.0
  res = n * (x ** (1/n) - 1)
  return res 


x = int(input())
print(f"natural logarithm(argument of the logarithm: {x}): {log(x)}")
# ==============================================


# ================== Method 2 ==================
import math

print(f"natural logarithm(argument of the logarithm: {x}): {math.log(x)}")
# ==============================================
