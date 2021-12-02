import numpy as np
import math

naturals = np.arange(1, 1000)
nat_sq = np.square(naturals)
triplets = []

for fsi, asq in enumerate(nat_sq):
  for ssi, bsq in enumerate(nat_sq):
    csq = asq + bsq 
    a = fsi+1
    b = ssi+1
    c = math.sqrt(csq)
    if c.is_integer():
      triplets.append([a, b, c])
      if (a+b+c)==1000:
        print(a,b,c)
        print(a*b*c)

