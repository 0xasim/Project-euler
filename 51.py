from primes import *
import numpy as np
import itertools

primeslist = set(psieve_list(10**4))
big_i, big_num = 0, 0

for i in itertools.count(10):
  na = np.array([int(px) for px in str(i)]) # [3 8 1 7]..
  print(i, na)
  for n in range(1, len(str(i))): # 1, 2 and 3 num of chars to replace
    num_of_primes = 0
    print(f'\tn = {n}')
    places = list(itertools.combinations(na, n))
    print(f'\tplaces {places}')
    for ep in places: # [0 1 2], [0 1 3], [0 2 3], ....,[1 2 3]
      print(f'\t\tep {ep}')
      for d in range(10):
        tna = int(''.join([str(xdc) for xdc in na]))
        na[list(ep)] = [d]*n
        print(f'\t\t\ttna {tna}')
        if(tna in primeslist): num_of_primes += 1

  print(f'num_of_primes {num_of_primes}')

