def sup(x_list, y_list):
  """
  the x corresponding to the maximum y 
  input  : x_list, y_list
  output : sup_x
  """
  max_y = max(y_list)
  max_y_idx = y_list.index(max_y)
  sup_x = x_list[max_y_idx]
  return sup_x

x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))
print(f"the x corresponding to the maximum y: {sup(x_list, y_list)}")
