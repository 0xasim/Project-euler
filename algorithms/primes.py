# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Use th algorithm above to get primes and not your bruteforce method
import itertools
import math
#import numba

def sieveOfErotosthenes(n):
  primes = {i for i in range(2, n)}
  p = 2
  while p < max(primes):
    for j in range(2, len(primes)):
      if ((prod := j*p) in primes):
        primes.remove(prod)
    p = min([i for i in primes if i > p])
  return primes

#@numba.jit
def lsieveOfErotosthenes(n):
  primes = [True for i in range(n)]
  primes[0], primes[1] = False, False
  for i in range(2, int(math.sqrt(n) + 1)):
    if primes[i]:
      tl = [j for v in range(n) if (j := i**2 + v*i) < n]
      for j in tl: primes[j] = False
  return ({ki for ki, k in enumerate(primes) if k is True})

def gen_primes():
  D = {}
  q = 2  # first integer to test for primality.
  while True:
    if q not in D:
      # not marked composite, must be prime  
      yield q 
      #first multiple of q not already marked
      D[q * q] = [q] 
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      # no longer need D[q], free memory
      del D[q]
    q += 1

# https://stackoverflow.com/a/19391111
# https://stackoverflow.com/a/10733621
def psieve():
  yield from (2, 3, 5, 7)
  D = {}
  ps = psieve()
  next(ps)
  p = next(ps)
  assert p == 3
  psq = p*p
  for i in itertools.count(9, 2):
    if i in D:      # composite
      step = D.pop(i)
    elif i < psq:   # prime
      yield i
      continue
    else:           # composite, = p*p
      assert i == psq
      step = 2*p
      p = next(ps)
      psq = p*p
    i += step
    while i in D:
        i += step
    D[i] = step

gen_primes_list = lambda lim: list(itertools.takewhile(lambda x: x < lim, gen_primes()))
gen_n_primes = lambda n: [p for _, p in zip(range(n), gen_primes())]

psieve_list = lambda lim: list(itertools.takewhile(lambda x: x < lim, psieve()))
psieve_n = lambda n: [p for _, p in zip(range(n), psieve())]

class isprime:
  def __init__(self, n, method = 'trialDiv'):
    self.n = n
    self.method = method
    self.bool = None
    if self.method == 'trialDiv': self.bool = self.trialDiv()
    
  def __bool__(self):
    return self.bool

  def trialDiv(self):
    if self.n <= 1: return False
    for i in range(2, int(math.sqrt(self.n)) + 1):
      if self.n % i == 0: return False
    return True

if __name__ == '__main__':
  from utils import call
  lim = 10**5

  ret1 = call(sieveOfErotosthenes, lim, pout=False)
  ret2 = call(lsieveOfErotosthenes, lim, pout=False)

  old = call(gen_n_primes, lim, pout=False)
  new = call(psieve_n, lim, pout=False)

  print(len(ret1), len(ret2), len(old), len(new))
  assert ret1 == ret2 == old == new

  print(isprime(4134514531).bool)

