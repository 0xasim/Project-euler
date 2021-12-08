import math
def series(n: int):
  total = 0
  for i in range(1, n + 1):
    total += i**i
  return str(total)[-10:]

from utils import call
call(series, int(10e2))
