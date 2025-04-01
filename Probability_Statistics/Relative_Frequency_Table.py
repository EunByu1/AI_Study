# ================== frequency table ==================
def freq_table(data):
  """
  Convert a list of data into a dictionary of frequencies 
  input  : data(list)
  output : data_freq(dictionary)
  """
  data_freq = {}
  keys = list(set(data))
  keys.sort()

  for key in keys:
    data_freq[key] = 0

  for value in data:
    data_freq[value] += 1
    
  return data_freq
# =====================================================
# ============= relative frequency table ==============
def freq2ratio(dic):
  """
  Convert a frequency dictionary to a relative frequency dictionary
  input : frequency dictionary dic
  output: relative frequency dictionary res
  """
  n   = sum(dic.values())
  res = {}
  
  for key in dic.keys():
    val = dic[key]
    res[key] = val/n
    
  return res
# =====================================================
data       = list(map(int, input().split()))
data_freq  = freq_table(data)
data_ratio = freq2ratio(data_freq)

print(f"data: {data}")
print(f"frequency table: {data_freq}")
print(f"relative frequency table: {data_ratio}")
