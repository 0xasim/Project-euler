import itertools
def primePerm(n: int):
  primes = primeSieve(10**n)
  hashPrimes = set(primes)
  for pi, p1 in enumerate(primes):
    for i in range(10 ** (n - 1), 10 ** n):
      if (p2 := i + p1) in hashPrimes and (p3 := i + p2) in hashPrimes:
        pset = [p1, p2, p3]
        p1Perms = set(itertools.permutations(str(p1), n))
        p1Perms = {int(''.join(s)) for s in p1Perms}
        for u in pset:
          if u not in p1Perms:
            break
        else:
          print(pset)
          print(''.join([str(s) for s in pset]))

import math
def primeSieve(l: int):
  ps = [True]*l
  ps[0] = ps[1] = False
  for x in range(2, int(math.sqrt(l) + 1)):
    if ps[x]:
      jays = [j for y in range(l) if (j := x**2 + y*x) < l]
      for j in jays: ps[j] = False
  return [pi for pi, p in enumerate(ps) if p]

from utils import call
call(primePerm, 4)

