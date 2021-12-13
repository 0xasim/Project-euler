from primes import *
import numpy as np
import itertools

primeslist = set(psieve_list(10**4))
big_i, big_num = 0, 0

for i in itertools.count(10):  # e-g: 3817
  na = np.array([int(px) for px in str(i)]) # [3 8 1 7]..
  for n in range(1, len(str(i))): # 1, 2 and 3 char positions to replace
    curri = 0
    for d in range(10): # 0-9
      places = list(itertools.combinations(list(str(i)), len(str(i))))
      print(i, places)
      for ep in places: # [0 1 2], [0 1 3], [0 2 3], ....,[1 2 3]
        print('here')
        na[list(ep)] = [d]*n
        if(int(na) in primeslist): current += 1

  if curri > big_i:
    big_i = curri
    print(big_i, big_num)

