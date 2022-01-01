import numpy as np
ispandigital = lambda n: all(np.arange(1, len(ns := str(n))+1) == [int(n) for n in sorted(ns)])

def primePan(stop):
  for w in range(stop, 10, -1):
    if ispandigital(w) and isprime(w): return w

import math
def isprime(n: int):
  if n <= 1: return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0: return False
  return True

from utils import call
call(primePan, 10**7)
