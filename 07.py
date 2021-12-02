from utils import timeMe

def getNthPrime(n):
  n -= 1 # 0 index
  prm_enc = 0 # Prime encounters
  prm_cnd = 2 # Prime candidate
  while prm_enc <= n:
    isprime = True
    for ed in range(2, prm_cnd):
      if prm_cnd % ed == 0:
        isprime = False
        break
    if isprime: prm_enc+=1
    prm_cnd += 1
  return prm_cnd-1



if __name__ == "__main__":
  print(timeMe(getNthPrime, 10001))
