import numpy as np
import math
import sys
sys.path.append('../algorithms')
from primes import *

def spiral_gen():
  # primes = psieve_list(10**4)
  spiral = list()
  spiral.append([1])
  n = 1
  while n < 10:
    print(n)
    outpoint = n**2
    next_outpoint = (n+2)**2
    layer = list(range(outpoint, next_outpoint))
    try:
      c = outpoint
      # right-bottom -> right-up
      for x in range(1, n+1):
        spiral[-x].append(outpoint+x)
      c += n
      # right-up -> left-up
      spiral.insert(0, list(range(c + n + 1 + 1, c, -1)))
      c += n + 1 + 1
      # left-up -> left-bottom
      ta = [c+x for x in range(1, n+1)][::-1]
      for x in range(1, n+1):
        spiral[-x].insert(0, ta[x-1])
      c += n + 1
      # left-bottom -> right-bottom
      spiral.append(list(range(c, c + n + 1 + 1)))
      pa(spiral)
    except IndexError:
      pa(spiral)
      raise IndexError
    print(f'\nlayer {layer}')
    n += 2

pa = lambda A: print('\n'.join([''.join(['{:4}'.format(item) for item in row])\
                  for row in A]))
if __name__ == '__main__':
  spiral_gen()

