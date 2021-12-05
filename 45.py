triNums = lambda lim: {eval('n * (n + 1) / 2') for n in range(1, lim +1)}
pentNums = lambda lim: {eval('n * (3*n - 1) / 2') for n in range(1, lim +1)}
hexNums = lambda lim: {eval('n * (2*n - 1)') for n in range(1, lim +1)}

def x(stop):
  tn, pn, hn = triNums(stop), pentNums(stop), hexNums(stop)
  for ti, t in enumerate(tn):
    if t in hn and t in pn:
        print(t)

from utils import call
call(x, 10**5)
