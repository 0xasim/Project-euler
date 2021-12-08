# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Use th algorithm above to get primes and not your bruteforce method

def sieveOfErotosthenes(n):
  primes = {i for i in range(2, n)}
  p = 2
  while p < max(primes):
    for j in range(2, len(primes)):
      if ((prod := j*p) in primes): primes.remove(prod)
    p = min([i for i in primes if i > p])
  return primes

import math
def lsieveOfErotosthenes(n):
  primes = [True for i in range(n)]
  primes[0], primes[1] = False, False
  for i in range(2, int(math.sqrt(n) + 1)):
    if primes[i]:
      tl = [j for v in range(n) if (j := i**2 + v*i) < n]
      for j in tl: primes[j] = False
  return ({ki for ki, k in enumerate(primes) if k is True})

def gen_primes():
  """ Generate an infinite sequence of prime numbers.
  """
  # Maps composites to primes witnessing their compositeness.
  # This is memory efficient, as the sieve is not "run forward"
  # indefinitely, but only as long as required by the current
  # number being tested.
  #
  D = {}

  # The running integer that's checked for primeness
  q = 2

  while True:
    if q not in D:
      # q is a new prime.
      # Yield it and mark its first multiple that isn't
      # already marked in previous iterations
      # 
      yield q
      D[q * q] = [q]
    else:
      # q is composite. D[q] is the list of primes that
      # divide it. Since we've reached q, we no longer
      # need it in the map, but we'll mark the next 
      # multiples of its witnesses to prepare for larger
      # numbers
      #
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      del D[q]

    q += 1

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
  ret2 = call(lsieveOfErotosthenes, lim, pout=False)
  ret1 = call(sieveOfErotosthenes, lim, pout=False)
  assert ret1 == ret2

  print(isprime(4134514531).bool)
