from utils import call
import itertools
from primes import *

def getPrimes(lim):
  global primes, sprimes
  sprimes = list(itertools.takewhile(lambda x: x < lim, gen_primes()))
  primes = set(sprimes)
  n = next(x[0] for x in enumerate(sprimes) if sum(sprimes[:x[0]+1]) > lim)
  sprimes = sprimes[:n + 1]

def euler50():
  gl, gs = 0, list()
  for pi, p in enumerate(sprimes):
    seq = list()
    for j in range(1000):
      if pi >= len(sprimes) - j - 1: break
      nex = sprimes[pi + j]
      seq.append(nex)
      if sum(seq) in primes and len(seq) > gl:
        gl, gs = len(seq), seq[:]
  return (gl, sum(gs))

call(getPrimes, 10**6)
call(euler50)
