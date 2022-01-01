from utils import call
import itertools
from primes import *

def getPrimes(lim):
  global primes_hash, primes_list
  primes_list = list(itertools.takewhile(lambda x: x < lim, gen_primes()))
  primes_hash = set(primes_list)
  n = next(x[0] for x in enumerate(primes_list) if sum(primes_list[:x[0]+1]) > lim)
  primes_list = primes_list[:n + 1]

def euler50():
  gl, gs = 0, list()
  for pi, p in enumerate(primes_list):
    seq = list()
    for j in range(1000):
      if pi >= len(primes_list) - j - 1: break
      nex = primes_list[pi + j]
      seq.append(nex)
      if sum(seq) in primes_hash and len(seq) > gl:
        gl, gs = len(seq), seq[:]
  return (gl, sum(gs))

call(getPrimes, 10**6)
call(euler50)
