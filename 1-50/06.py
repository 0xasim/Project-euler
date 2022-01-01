def sumofsq(n):
  return sum([en**2 for en in range(n+1)])
def sqofsum(n):
  return (sum([en for en in range(n+1)])**2)

if __name__ == "__main__":
  n = 100
  print(sqofsum(n)-sumofsq(n))
