def triNumSeq(n, func):
  i = 2
  prev = 1
  while True:
    c = prev+i
    if func(c) > n: return c
    i += 1
    prev = c

def factorize(n):
  factors = 0+1
  for i in range(1, int(n/2)+1):
    if n%i == 0: factors+=1
  return factors

def divisors(x):
    limit = x
    numberOfDivisors = 0
    if (x == 1): return 1
    i = 1
    while i < limit:
      if (x % i == 0):
        limit = x / i;
        if (limit != i):
          numberOfDivisors+=1
        numberOfDivisors+=1
      i+=1
    return numberOfDivisors

def ndivisors(n):
    count = 2  # accounts for 'n' and '1'
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            count += 2
        i += 1
    if i ** 2 == n:
        count += 1
    return count

import operator, functools
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return functools.reduce(operator.mul, powers_plus, 1)

if __name__ == "__main__":
  d = 100
  from utils import call
  a = call(triNumSeq, d, divisors)
  b = call(triNumSeq, d, factorize)
  c = call(triNumSeq, d, ndivisors)
  d = call(triNumSeq, d, NumberOfDivisors)
  assert a == b == c
