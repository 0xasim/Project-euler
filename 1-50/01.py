def multiples_3or5(limit):
  result = []
  for nn in range(1, limit):
    if nn%5==0 or nn%3==0:
      result.append(nn)
  return sum(result)

if __name__ == "__main__":
  r = multiples_3or5(1000)
  print(r)
