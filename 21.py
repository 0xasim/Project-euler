def amicable_nums(lim):
  amics = list()
  for ac in range(lim):
    if is_amicable(ac): amics.append(ac)
  return sum(amics)

def is_amicable(n):
  if n == sum(divisors(sum(divisors(n)))) and n != sum(divisors(n)):
    return True
  return False

import functools
@functools.cache
def divisors(m):
  divisors = list()
  for i in range(1, int(m/2)+1):
    if m % i == 0:
      divisors.append(i)
  return divisors
    
from utils import call
call(amicable_nums, 10000)
