ispandigital = lambda prod, mpcant, mplier:\
  ''.join(sorted(str(prod) + str(mpcant) + str(mplier))) == '123456789'

def allpandigitals():
  prods = set()
  for i in range(2000):
    for j in range(500):
      if len(str(i*j)) == 4 and i*j not in prods \
                      and ispandigital(i*j, i, j): prods.add(i*j)
  return sum(prods)
  
from utils import call
call(allpandigitals)
