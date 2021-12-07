# Consecutive DPS
def consDPF(nf):
  i = 0
  while True:
    if all([len(set(factorize(c))) == nf for c in range(i, i + nf)]):
      return [i+a for a in range(nf)]
    i += 1

import functools
@functools.cache
def factorize(n: int):
  sortedSP = sorted(sieve_primes)
  fs = list()
  for i in sortedSP:
    if n % i == 0:
      fs.append(i)
  return fs

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
sieve_primes = set(call(primeSieve, int(1e3), pout=False))
call(consDPF, 4)
