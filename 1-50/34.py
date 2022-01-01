import functools
@functools.cache
def factorial(n: int):
  if n <= 1: return 1
  return n * factorial(n-1)

from utils import call
curious_nums = call(lambda: sum([n for n in range(3,10**6)\
      if sum([factorial(int(s)) for s in str(n)]) == n]))
