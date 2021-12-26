from primes import *
import numpy as np
import itertools

primeslist = set(psieve_list(10**6))
max_primes = 0

# for i in itertools.count(10):
iters = [56003, 120303] 
#for i in range(56000, 56003):
for i in iters:
  if i%1000==0: print(i)
  na = np.array([int(px) for px in str(i)]) # [3 8 1 7]..
  print(i, na)
  for replace_count in range(1, len(str(i))): # Num of chars to replace (1, 2 and 3)
    print(f'\treplace_count = {replace_count}')
    places = list(itertools.combinations(np.arange(len(na)), replace_count))
    print(f'\tplaces {places}')
    for ep in places: # [0 1 2], [0 1 3], [0 2 3], ....,[1 2 3]
      num_of_primes = 0
      print(f'\t\tep {ep}')
      drange = range(10)
      if ep[0] == 0: drange = range(1,10) 
      for d in drange:
        tna = na.copy()
        tna[list(ep)] = [d]*replace_count
        print(f'\t\t\ttna {tna}')
        if int(''.join([str(tt) for tt in tna])) in primeslist:
          print(f'\t\t\t\t this tna is a prime')
          num_of_primes += 1
      # print(f'num_of_primes {num_of_primes}')
      if num_of_primes > max_primes:
        max_primes = num_of_primes
        print(i, max_primes, 'found'*10)

