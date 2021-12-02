from utils import call

import functools
@functools.cache
def factorial(n):
  if n == 1: return 1
  return n * factorial(n-1)

print(sum([int(d) for d in str(factorial(100))]))
