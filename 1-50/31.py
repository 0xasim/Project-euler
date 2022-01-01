from tqdm import tqdm

def coin_sums(zz):
  coins = [1, 2, 5, 10, 20, 50, 100, 200]
  exp = 'j*2 + k*5 + l*10 + m*20 + n*50 + o*100 + p*200'
  count = 1
  for p in range(1):
    for o in tqdm(range(2+1)):
      for n in range(4+1):
        for m in range(10+1):
          for l in range(20+1):
            for k in range(40+1):
              for j in range(100+1):
                if eval(exp) <= zz:
                  count += 1
                  #print(j,k,l,m,n,o,p, f'count: {count}')
  return count

# https://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
def mathblogdotdk(target = 200):
  ways = 0
  for a in range(target, -1, -200):
    for b in range(a, -1, -100):
      for c in range(b, -1, -50):
        for d in range(c, -1, -20):
          for e in range(d, -1, -10):
            for f in range(e, -1, -5):
              for g in range(f, -1, -2):
                ways += 1
  return ways

from utils import call
call(mathblogdotdk, 200)
call(coin_sums, 200)
