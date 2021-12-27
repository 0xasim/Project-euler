import itertools
sn = lambda n: sorted([int(i) for i in str(n)])

for x in itertools.count(1):
  x2, x3, x4, x5, x6 = x*2, x*3, x*4, x*5, x*6
  if sn(x) == sn(x2) == sn(x3) == sn(x4) == sn(x5) == sn(x6):
    print(x)
    break
