import numpy as np
# Consecutive DPF
def consDPF(nf):
	i = 1
	while True:
		cDFS = [countDistFactors(c) == nf for c in range(i, i + nf)]
		if all(cDFS):
			return [i+a for a in range(nf)]
		i += [i for ii, i in enumerate(cDFS) if not i][-1] + 2

# Distinct Prime Factors (DPF)
import functools
@functools.cache
def countDistFactors(n: int):
	dfs = 0
	for i in sortedSP:
		if not n % i:
			dfs += 1
			while n % i == 0:
				n /= i
	return dfs

# Sieve of Eratosthenes
import math
def primeSieve(stop: int):
	pool = [True for _ in range(stop)]
	pool[0], pool[1] = False, False
	for i in range(2, int(math.sqrt(stop) + 1)):
		if pool[i]:
			jays = (j for x in range(stop) if (j:= i**2 + x*i) < stop)
			for j in jays: pool[j] = False
	return {zi for zi, z in enumerate(pool) if z}

if __name__ == '__main__':
	from utils import call
	sieve_primes = set(call(primeSieve, int(1e3), pout=False))
	sortedSP = sorted(sieve_primes)
	call(consDPF, 4)
