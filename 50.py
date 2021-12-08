from utils import call
from primes import lsieveOfErotosthenes

def getPrimes(lim):
  global primes, sprimes
  primes = call(lsieveOfErotosthenes, lim, pout=False)
  sp = sorted(primes)
  n = next(x[0] for x in enumerate(sp) if sum(sp[:x[0]+1]) > lim)
  sprimes = sp[:n + 1]

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
        print(p, gl, sum(gs))
  return (gl, sum(gs))

call(getPrimes, 10**6)
call(euler50)
