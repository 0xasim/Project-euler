import sys, time
sys.path.append('../algorithms')

import primes
pl = primes.psieve_list(10**4)

import functools, math
@functools.cache
def f(x, y):
  a = math.floor(math.log10(y))
  return int(x*10**(1+a)+y)

def pair_primes(pair):
  return primes.is_prime(f(pair[0],pair[1])) and primes.is_prime(f(pair[1],pair[0]))
lp = lambda ls: all([pair_primes(ts) for ts in ls])

import itertools
combs = itertools.combinations(pl, 4)
from tqdm import tqdm
S = time.time()
def main():
  for l in pl:
    for m in pl:
      if l==m: continue
      if not lp([(l,m)]): continue
      for n in pl:
        if l==n or m==n: continue
        if not lp([(l,n), (m,n)]): continue
        for o in pl:
          if l==o or m==o or n==o: continue
          if not lp([(l,o), (m,o), (n,o)]): continue
          for p in pl:
            if l==p or m==p or n==p or o==p: continue
            if not lp([(l,p), (m,p), (n,p), (o,p)]): continue
            else:
              print(f"found: {[l, m, n, o, p], {sum([l,m,n,o,p])}}")
              return
main()
print(time.time() - S)
