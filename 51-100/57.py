
import sys
sys.setrecursionlimit(2000)

from fractions import Fraction
def series(i):
  if i > 0:
    i -= 1
    return Fraction(1, 2 + series(i))
  return 0

sqrc = lambda x: 1 + series(x)

def euler57():
  count = 0
  for n in range(1, 1001):
    res = sqrc(n)
    nom, denom = res.as_integer_ratio()
    if len(str(nom)) > len(str(denom)): count += 1
  return count

from utils import call
call(euler57)
