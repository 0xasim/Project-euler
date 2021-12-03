from itertools import count

def quadratic_primes():
  qf = "n**2 + a*n + b"
  max_primes = 0
  max_primes_vars = dict()

  for a in range(-1000, 1000):
    for b in range(-1000, 1000+1):
      primes = 0
      for n in count():
        if not isprime(eval(qf)): break
        primes += 1
      if primes > max_primes:
        max_primes = primes
        max_primes_vars = {"a" : a, "b" : b}
        print (max_primes, max_primes_vars)

  return (max_primes_vars['a'] * max_primes_vars['b'])

def isprime(n):
  prime = True
  if n <=1: return False
  for i in range(2, 3000):
    if n % i == 0 and n != i:
      prime = False
      break
  return prime

from utils import call
call(quadratic_primes)

