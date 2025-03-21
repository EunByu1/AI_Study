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

def combination(x, n):
    """
    combination function
    input  : 정수 x, n
    output : 출력값: nCx(실수)
    """
    res = factorial(x)/(factorial(x-n)*factorial(n))
    return res

x, n = map(int, input().split())
print(f"combination {x}C{n}: {combination(x,n)}")
