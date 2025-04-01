# ====================== Algorithm ======================
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
print(f"data: {x_list}, mean(using algorithm): {mean(x_list)}")
# =======================================================

# ======================== NumPy =======================
import numpy as np 

x_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
mean_x = np.mean(x_list)
print(f"data: {x_list}, mean(using numPy): {mean(x_list)}")
# =======================================================
