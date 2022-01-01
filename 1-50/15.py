import numpy as np
from utils import *
import functools

def possible_routes(x, y):
  @functools.cache
  def traverse(i, j):
    if (i, j) == (x-1, y-1): return 1
    else:
      if j+1 <= y-1 and i+1 <= x-1:
        return traverse(i, j+1) + traverse(i+1, j)
      elif i+1 <= x-1:
        return traverse(i+1, j)
      elif j+1 <= y-1:
        return traverse(i, j+1)
      return 0
  x, y = (x+1, y+1)
  return traverse(0, 0)

call(possible_routes,20,20)
