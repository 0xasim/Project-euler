triangle = lambda n: n * (n + 1) / 2
square = lambda n: n ** 2
pentagonal = lambda n: n * (3 * n - 1) / 2
hexagonal = lambda n: n * (2 * n - 1)
heptagonal = lambda n: n * (5 * n - 3) / 2
octagonal = lambda n: n * (3 * n - 2)

polygonals = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
pL = [[int(p(n)) for n in range(1, 150)] for p in polygonals]
pL = [[str(t) for t in p if len(str(t)) == 4] for p in pL]
def isSpecial(s, strict=False):
  for i in range(ls := len(s)):
    j = i+1
    if j > ls - 1:
      if not strict: continue
      j = 0
    if not s[i][2:] == s[j][:2]:
      return False
  return True

import itertools
prod1 = itertools.product(pL[0], pL[1], pL[2])
prod2 = itertools.product(pL[3], pL[4], pL[5])
from tqdm import tqdm
def cyclics(prod):
  thrs = list()
  for p in tqdm(prod):
    pers = itertools.permutations(p)
    for s in pers:
      if isSpecial(s):
        thrs.append(s)
  return thrs
c1 = cyclics(prod1)
c2 = cyclics(prod2)

for s1 in c1:
  for s2 in c2:
    if isSpecial(sc := list(s1)+list(s2), strict=True):
      print(sc, sum([int(t) for t in sc]))
      break
