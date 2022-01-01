from fractions import Fraction
import sys
sys.setrecursionlimit(2000)

def series(i):
  if i > 0:
    i -= 1
    return Fraction(1, 2 + series(i))
  return 0

sqrc = lambda x: 1 + series(x)
count = 0
for n in range(1, 1001):
  res = sqrc(n)
  nom, denom = res.as_integer_ratio()
  if len(str(nom)) > len(str(denom)): count += 1

print(f'count: {count}')

