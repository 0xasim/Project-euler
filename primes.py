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
