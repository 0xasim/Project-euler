from sympy import isprime
'strings are the problem, learn to rotate without them'
iscircularprime = lambda n:\
    isprime(n) and all([isprime(int(str(n)[i:]+str(n)[:i]))\
              for i in range(len(str(n)))])

'use sieve (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to get the primes
not this dump thing'
import functools
@functools.cache
def isprime_bf(n: int):
  if n <= 1: return False
  elif n % 2 == 0: return False
  for i in range(2, int(n/2)+1):
    if n % i == 0 and n != i: return False
  return True

isprime = isprime_bf
circ_under_mill = lambda below: len([n for n in range(below) if iscircularprime(n)])
from utils import call
call(circ_under_mill, 10**5)
