# Here to prove Goldbach wrong
expr = 'eoc == epr + 2 * n**2'
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
            'oc' : {yi for yi, y in enumerate(pool) if not y and yi % 2} # odd composites
    })

def falseConj():
  ps = primeSieve(10**7)
  primes, oc = ps['primes'], ps['oc']
  ocied = [False for i in range(len(oc))]
  for eoci, eoc in enumerate(oc):
    for epr in primes:
      for n in range(1,100):
        if (ev := eval(expr) in oc): 
          ocied[eoci] = True
          break
      if ev > eoc: break  #eval > odd composite
    if ocied[eoci]: break
  return [(oi, o) for o in enumerate(ocied) if not o]


from utils import call
call(falseConj)
