# ====================== Mean Algorithm ======================
def mean(x_list):
  """
  Find the average of the elements of the list x_list
  input : list(x_list)
  output: mean(res)
  """
  n     = len(x_list)
  sum_x = 0

  for x in x_list:
    sum_x += x
  res = sum_x/n
    
  return res

x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
print(f"data: {x_list}")
print(f"mean(using algorithm): {mean(x_list)}")
# =======================================================


# ================== Variance Algorithm =================
def var(x_list):
  """
  Find the variance of the elements of the list x_list
  input : list(x_list)
  output: variance(res)
  """
  n      = len(x_list)
  mean_x = mean(x_list)
  ss_x   = 0

  for x in x_list:
    ss_x += (x-mean_x)**2
  res = ss_x/(n-1)
    
  return res

x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
print(f"variance(using algorithm): {var(x_list)}")
# =======================================================

# ============= Standard Deviation Algorithm ============
def std(x_list):
  """
  Find the standard deviation of the elements of the list x_list
  input : list(x_list)
  output: standard deviation(res)
  """
  var_x = var(x_list)
  res   = var_x**0.5
    
  return res

x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
print(f"standard deviation(using algorithm): {std(x_list)}")
# =======================================================

# ======================== NumPy ========================
import numpy as np 

x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]

var_x = np.var(x_list, ddof=1)
std_x = np.std(x_list, ddof=1)

print(f"variance(using numpy): {var_x}")
print(f"standard deviation(using numpy): {std_x}")
# =======================================================
