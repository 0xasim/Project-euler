# Here to prove Goldbach wrong
import math
def primeSieve(stop: int):
  pool = [True for _ in range(stop)]
  pool[0], pool[1] = False, False
  for i in range(2, int(math.sqrt(stop) + 1)):
    if pool[i]:
      jays = (j for x in range(stop) if (j:= i**2 + x*i) < stop)
      for j in jays: pool[j] = False
  return ({
         'primes': [zi for zi, z in enumerate(pool) if z],
            'oc' : [yi for yi, y in enumerate(pool) if not y and yi % 2] # odd composites
          })

from utils import call
def falseConj():
  ps = call(primeSieve, 10**4 , pout=False)
  primes, oc = ps['primes'], ps['oc'][1:] 

  for eoc in oc:
    found = False
    for epr in primes:
      if found: break
      for n in range(1,100):
        if eoc == epr + 2 * n**2: 
          found = True
          break
    if not found: return eoc

call(falseConj)
