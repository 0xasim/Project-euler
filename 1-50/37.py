import functools, math
@functools.cache
def isprime(n: int):
  if n <= 1: return False
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0 and n != i: return False
  return True

def isTrunctable(n):
  for ci, _ in enumerate(ns := str(n)):
    if not (isprime(int(ns[ci:])) and isprime(int(ns[:ci+1]))): return False
  return True

def trunctablePrimes(lim):
  tps = list()
  for n in range(10, lim):
    if isTrunctable(n): tps.append(n)
  return (tps, sum(tps))

from utils import call
call(trunctablePrimes, 10**6)
