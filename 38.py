import numpy as np
ispandigital = lambda n: ''.join(sorted(str(n))) == '123456789'

from itertools import count
def panDigiMul(lim):
  pans = list()
  for u in range(lim):
    conc = str()
    for v in count(1):
      conc += (ms := str(u*v))
      if len(conc) > 9: break 
      if ispandigital(conc): pans.append((conc, u, v))
  return max(i[0] for i in pans)

from utils import call
call(panDigiMul, 10**6)
