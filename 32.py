ispandigital = lambda prod, mpcant, mplier:\
  ''.join(sorted(str(prod) + str(mpcant) + str(mplier))) == '123456789'

def allpandigitals():
  prods = set()
  for i in range(10000):
    for j in range(1000):
      if ispandigital(i*j, i, j) and i*j not in prods: prods.add(i*j)
  return sum(prods)
  
from utils import call
call(allpandigitals)
