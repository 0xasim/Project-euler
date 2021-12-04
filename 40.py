lim = 10**6
df = lambda lim: ''.join([str(i) for i in range(0, lim + 1)])
d = df(lim)

n, prod = 1, 1
while n <= lim:
  prod *= int(d[n])
  n *= 10
print(f'product: {prod}')

