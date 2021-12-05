# Here to prove Goldbach wrong
expr = 'oc == pr + 2 * n**2'
import math
def primeSieve(stop: int):
  pool = [True for _ in range(stop + 1)]
  pool[0], pool[1] = False, False
  for p in range(2, int(math.sqrt(stop) + 1)):
    for q in range(2, stop + 1):
      if (pq := p * q) <= stop: pool[pq] = False
  print(pool)

primeSieve(10)
