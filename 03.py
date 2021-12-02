def lprime_factor(n):
  factors = []
  f = 2
  while f < 1000000:
    if n%f == 0 and isprime(f)[0]:
      n//=f
      factors.append(f)
    else: f+=1
    if isprime(n)[0]:
      factors.append(n)
      print(f"Breaking on {n}")
      break
  return factors

def isprime(n):
  for en in range(2, n):
    if n % en == 0: return [False, en]
  return [True]
  
if __name__ == "__main__":
  print(isprime(13195))
  r = lprime_factor(13195)
  print(r)
  r = lprime_factor(600851475143)
  print(r)
