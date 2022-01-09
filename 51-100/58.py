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
  while n <= 3:
    print(n)
    outpoint = n**2
    next_outpoint = (n+2)**2
    layer = list(range(outpoint, next_outpoint))
    try:
      c = outpoint
      for x in range(1, n+1):
        spiral[-x].append(outpoint+x)
      c = c + 1
      spiral.insert(0, list(range(c+3, c, -1)))
      c = c + outpoint + 2
      for x in range(1, n+1):
        spiral[-x].insert(0, c+x)
      c = c + outpoint + 1
      spiral.append(list(range(c, c+3)))
      print(f'spiral {spiral}')
    except IndexError:
      print(f'spiral {spiral}')
      raise IndexError
    print(f'layer {layer}')
    n += 2
  print(spiral)

if __name__ == '__main__':
  spiral_gen()

