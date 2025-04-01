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
# =======================================================

# ================= Covariance Algorithm ================
x1_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
x2_list = [3, 1, 2, 7, 3, 8, 3, 4, 5]

print(f"x1_list: {x1_list}")
print(f"x2_list: {x2_list}")

n  = len(x1_list)
m1 = mean(x1_list)
m2 = mean(x2_list)
sm = 0

for i in range(0,n):
  sm += (x1_list[i]-m1)*(x2_list[i]-m2)

covariance = sm/(n-1)
print(f"covariance(using algorithm): {covariance}")
# =======================================================

# ========== Correlation Coefficient Algorithm ==========
std1 = std(x1_list)
std2 = std(x2_list)

corr = covariance/(std1*std2)
print(f"correlation coefficient(using algorithm): {corr}")
# =======================================================

# ================= Cov & Corr Function =================
def cov(x1_list, x2_list):
  """
  Find the covariance of the elements of the list x_list
  input : list(x_list)
  output: covariance(res)
  """
  n  = len(x1_list)
  m1 = mean(x1_list)
  m2 = mean(x2_list)
  sm = 0

  for i in range(0,n):
    sm += (x1_list[i]-m1)*(x2_list[i]-m2)

  res = sm/(n-1)

  return res


def corr(x1_list, x2_list):
  """
  Find the correlation coefficient of the elements of the list x_list
  input : list(x_list)
  output: correlation coefficient(res)
  """
  covariance = cov(x1_list, x2_list)
  std1 = std(x1_list)
  std2 = std(x2_list)
  res = covariance/(std1*std2)
  
  return res


x1_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
x2_list = [3, 1, 2, 7, 3, 8, 3, 4, 5]

print(f"x1_list: {x1_list}")
print(f"x2_list: {x2_list}")

covariance = cov(x1_list, x2_list)
corrcoef   = corr(x1_list, x2_list)

print(f"covariance(using algorithm): {covariance}")
print(f"correlation coefficient(using algorithm): {corrcoef}")
# =======================================================

# ======================== NumPy ========================
import numpy as np 

x1_list = [2, 4, 6, 1, 5, 7, 9, 8, 3]
x2_list = [3, 1, 2, 7, 3, 8, 3, 4, 5] 

covariance = np.cov(x1_list, x2_list)
print(f"covariance(using numpy): {covariance}")

corr = np.corrcoef(x1_list, x2_list)
print(f"correlation coefficient(using numpy): {corr}")
# =======================================================
