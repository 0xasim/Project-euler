
pantagonals = lambda stop: {int(eval('n * (3 * n - 1) / 2')) for n in range(1, stop + 1)}

def x(stop):
  pantNums = pantagonals(stop)
  plist = list(pantNums)
  dees = list()
  for ji, j in enumerate(plist):
    for k in plist:
      if (j + k) in pantNums and (d := abs(j - k)) in pantNums\
          and j != k:
            dees.append(d)
  print(dees)
  return min(dees)

print(sorted(pantagonals(10)))
from utils import call
call(x, 10**4)
