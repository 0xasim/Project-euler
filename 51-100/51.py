from primes import *
import numpy as np
import itertools

def prime_dig_replace(primeslist, lim=8):
  for i in itertools.count(56003):
    na = np.array([int(px) for px in str(i)]) # [3 8 1 7]..
    for replace_count in range(1, len(str(i))): # Num of chars to replace (1, 2 and 3)
      places = list(itertools.combinations(np.arange(len(na)), replace_count))
      for ep in places: # [0 1 2], [0 1 3], [0 2 3], ....,[1 2 3]
        num_of_primes = 0
        plist = list()
        drange = range(10)
        if ep[0] == 0: drange = range(1,10) 
        for d in drange:
          if d >= 3 and num_of_primes < 2: break
          tna = na.copy()
          tna[list(ep)] = [d]*replace_count
          tnum = int(''.join([str(tt) for tt in tna]))
          if tnum in primeslist:
            num_of_primes += 1
            plist.append(tnum)
        if num_of_primes >= lim:
          return min(plist)

from utils import call
primeslist = set(call(psieve_list, 10**6, pout=False))
call(prime_dig_replace, primeslist, pin=False)

