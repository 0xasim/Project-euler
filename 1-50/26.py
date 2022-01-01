from decimal import *
getcontext().prec = 5000

def reciprocal_cycle(den):
  # is giviing 16 fp precision
  dec_frac = str(Decimal(1) / Decimal(den))[2:]   # disinclude 0.1
  if len(dec_frac) == 1: return 1
  # unnecessary?
  if all([j == dec_frac[0] for j in dec_frac]): return "inf" # slowing factor
  cycle = str()
  for index, i in enumerate(dec_frac):
    if cycle:
      if cycle == dec_frac[index:index+len(cycle)]: 
        jump = len(cycle)
        if cycle == dec_frac[index+jump:index+len(cycle)+jump]:
          break
    cycle += i

  if len(cycle) >= 1000: return "inf"
  return len(cycle)

def max_d():
  l, d = 0, 0
  for i in range(2, 1000):
    res = reciprocal_cycle(i)
    # print(f'1/{i} = {res}')
    if res != 'inf':
      if res > l:
        l = res
        d = i
  return d
    
# Not my solution
def ex26():
  maxlen = 0
  for n in range(2, 1000):
    rest = 1
    for i in range(n): rest = (rest*10)%n
    r0 = rest
    length = 0
    while True:
      rest = (rest*10)%n
      length+=1
      if rest == r0: break
    if length > maxlen:
      maxn = n
      maxlen = length
  print(f"ex26: ${maxn}: {maxlen}")
  return maxn


from utils import call
call(max_d)
call(ex26)

