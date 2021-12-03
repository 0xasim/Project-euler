def IsPalindromic(n):
  n = str(n)
  if n[::-1] == n: return True
  return False

def decToBin(n):
  bins = str()
  def convert(n):
    nonlocal bins
    if n >= 1: convert(n // 2)
    bins += str(n % 2)
    return bins
  return str(int(convert(n)))
  
print(sum([n for n in range(10**6) if IsPalindromic(n) and IsPalindromic(decToBin(n))]))
