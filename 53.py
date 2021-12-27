def factorial(x):
  t = 1
  while x > 1:
    t *= x
    x -= 1
  return t

ncr = lambda n, r: int(factorial(n) / (factorial(r) * factorial(n-r)))
milplus = 0
for n in range(1, 100+1):
  for r in range(n):
    if ncr(n, r) > 10**6:
      milplus += 1

print(milplus)
