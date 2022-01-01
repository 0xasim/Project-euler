def palindrome(ndigits):
  pals = []
  for fd in range(int(str(9)*ndigits)+1, int(str(9)*(ndigits-1))+1, -1):
    for sd in range(int(str(9)*ndigits)+1, int(str(9)*(ndigits-1))+1, -1):
      prod = fd*sd
      if ispalindromic(prod): pals.append(prod)
  return max(pals)

def ispalindromic(n):
  if str(n)[::-1] == str(n): return True
  return False

if __name__ == "__main__":
  print(palindrome(3))
  
  
