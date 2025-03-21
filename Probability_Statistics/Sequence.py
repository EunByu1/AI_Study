def seq(start, stop, step):
  """
  sequence function 
  input  : start(시작 값), stop(끝 값), step(한 스텝당 증가 수)
  output : res(리스트)
  """
  res = []
  current = start
  while current < stop:
    res.append(current)
    current += step
  return res


start, stop, step = map(int, input().split())
print(f"sequence(start:{start},stop:{stop},step:{step}): {seq(start, stop, step)}")
