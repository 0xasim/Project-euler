# Here to prove Goldbach wrong

import math
def primeSieve(stop: int):
  pool = [True for _ in range(stop)]
  pool[0], pool[1] = False, False
  for i in range(2, int(math.sqrt(stop) + 1)):
    if pool[i]:
      jays = (j for x in range(stop) if (j:= i**2 + x*i) < stop)
      for j in jays: pool[j] = False
  return [zi for zi, z in enumerate(pool) if z]

def falseConj():
  primes = primeSieve(10**4)
  oddComposites = [y for y in range(2, 10**4) if y % 2 and y not in primes] 

  for eoc in oddComposites:
    for epr in primes:
      if (t := (eoc - epr) / 2) < 0:
        return eoc
      if (n := math.sqrt(t)) - int(n) < 0.00001:
        break
  return None

from utils import call
call(falseConj)
