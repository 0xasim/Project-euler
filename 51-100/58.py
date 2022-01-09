import numpy as np
import math
import sys
sys.path.append('../algorithms')
from primes import *

def spiral_gen():
  # primes = psieve_list(10**4)
  spiral = list()
  n = 1
  while n <= 10:
    m = n + len(spiral)
    spiral.append([i for i in range(n)])
    spiral.insert(spiral[n-1][0], [n+1])
    n += 2

  print(spiral)

if __name__ == '__main__':
  spiral_gen()

