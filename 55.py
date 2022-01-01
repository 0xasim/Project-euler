def rev(n: int):
  r = 0
  while n > 0:
    r = (r * 10) + (n % 10)
    n //= 10
  return r

ispalin = lambda d: d == rev(d)

lychrel, done = list(), set()
for n in range(10, 10001):
  t = n
  if t not in done:
    for i in range(51):
      if ispalin(s := (t + rev(t))):
        done.add(t)
        break
      t = s
    else: lychrel.append(n)

print(len(lychrel))
