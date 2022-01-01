maxSum = 0
for a in range(100):
  for b in range(100):
    s = sum([int(i) for i in str(a**b)])
    if s > maxSum: maxSum = s
print(maxSum)
