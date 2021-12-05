import numpy as np
div = [2, 3, 5, 7, 11, 13, 17]
prop = lambda pg: all([int(str(pg)[n:n+3]) % div[n-1] == 0 for n in range(1, len(str(pg))-2)])

import itertools
def permY():
  perms = itertools.permutations('0123456789', r=10)
  return sum([int(sep) for ep in perms if prop((sep := ''.join(ep)))])

from utils import call
call(permY)
