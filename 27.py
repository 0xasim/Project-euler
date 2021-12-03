def quadratic_primes():
  qf = "n**2 + a*n + b"
  max_primes = 0
  max_primes_vars = dict()

  for a in range(-1000, 1000):
    for b in range(-1000, 1000+1):
      print(a, b)
      primes = 0
      for n in range(100):
        if not isprime(eval(qf)): break
        primes += 1
      if primes > max_primes:
        max_primes = primes
        max_primes_vars = {"a" : a, "b" : b}
        print (max_primes, max_primes_vars)

  return (max_primes, max_primes_vars)

isprime = lambda n: True if all([n % i != 0 for i in range(1, int(n/2)+1)]) else False

from utils import call
call(quadratic_primes)

