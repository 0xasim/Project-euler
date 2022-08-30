total_n = 0
for i in range(1000):
  for j in range(1000):
    if len(str(powd := i**j)) == j:
      print(i, j, powd)
      total_n += 1
print(total_n)
