import numpy as np
import math
ispandigital = lambda n: all(np.arange(1, len(ns := str(n))+1) == [int(n) for n in sorted(ns)])
def primeSieve(n: int):
  i, primes = 2, [True for _ in range(2, n + 1)]
  while i <= len(primes) -1:
    for x in range(2, int(math.sqrt(n) + 1):
      if x > n - 1: break
      primes[x] = False
    i = min([vi for vi, v in enumerate(primes) if vi > i and v = True])
  return primes

print(ispandigital(2143))
