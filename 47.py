# Consecutive DPS
def consDPF(nf):
  i = 0
  while True:
    if all([DPF(c) == nf for c in range(i, i + nf)]):
      return [i+a for a in range(nf)]
    i += 1

# Distinct Prime Factors (DPF)
def DPF(n: int):
  dist_fact = set(factorize(n))
  if dist_fact:
    allprimes = all([inPS(f) for f in dist_fact])
    if not allprimes: return None
    return len(dist_fact)
  return None

import functools
@functools.cache
def factorize(n: int):
  factors = list()
  def calc(x: int):
    if x <= 1: return x
    for i in range(2, int(x/2) + 1):
      if x % i == 0:
        factors.append(i)
        return calc(x / i)
    factors.append(int(x))
  calc(n)
  return factors

import math
@functools.cache
def isprime(y: int):
  if y <= 1: return False
  for i in range(2, int(math.sqrt(y) + 1)):
    if y % i == 0:
      return False
  return True

import math
def primeSieve(stop: int):
  pool = [True for _ in range(stop)]
  pool[0], pool[1] = False, False
  for i in range(2, int(math.sqrt(stop) + 1)):
    if pool[i]:
      jays = (j for x in range(stop) if (j:= i**2 + x*i) < stop)
      for j in jays: pool[j] = False
  return [zi for zi, z in enumerate(pool) if z]
   
from utils import call
sieve_primes = set(call(primeSieve, 10**4, pout=False))
inPS = lambda pc: pc in sieve_primes
call(consDPF, 4)




