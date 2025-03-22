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

data = list(map(int, input().split()))
print(f"data: {data}, frequency table: {freq_table(data)}")
