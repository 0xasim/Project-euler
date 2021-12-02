def sum_of_primes(lim):
  sum = 0
  for i in range(2, lim):
    if isprime(i): sum+=i
  return sum

def isprime(n):
  for i in range(2, 3000):
    if n%i==0 and n!=i: return False
  return True

print(sum_of_primes(2000000))
