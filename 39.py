def pSolutions(p):
  pees = set()
  for a in range(1, p):
    for b in range(1, p-a):
      c = p - (a+b)
      if a**2 == b**2 + c**2:
        pees.add(tuple(sorted((a,b,c))))
  return len(pees)

import math
def pSolutions2(p):
  top = 0
  for a in range(int(p/4)):
    for b in range(a+1, int((p-a)/2)):
      c = math.sqrt(a**2 + b**2)
      if a + b + c == p: top += 1
  return top

def maxP(lim):
  mp, mpr = 0, 0
  for p in range(lim+1):
    if (r := pSolutions2(p)) > mpr:
      mpr = r
      mp = p
  return (mp, mpr)

from utils import call
call(maxP, 1000)
