import numpy as np
import sympy

def spiral_primes():
  spiral = [[1]]
  n_diag_primes, n = 0, 1

  while True:
    c_diags = list()
    c = outpoint = n**2
    next_outpoint = (n+2)**2
    layer = list(range(outpoint, next_outpoint))
    try:
      # bottom-right -> top-right
      for x in range(1, n+1):
        spiral[-x].append(c + x)
      c += n

      # top-right -> top-left
      spiral.insert(0, list(range(c + n + 1 + 1, c, -1)))
      c += n + 1 + 1
      c_diags.extend([spiral[0][0], spiral[0][-1]])

      # top-left -> bottom-left
      '''  Tryna save compute
      ta = [c+x for x in range(1, n+1)][::-1]
      for x in range(1, n+1):
        spiral[-x].insert(0, ta[x-1])
      c += n + 1
      '''
      # bottom-left-> bottom-right
      spiral.append(list(range(c, c + n + 1 + 1)))

      c_diags.extend([spiral[-1][0], spiral[-1][-1]])
      n_diag_primes += sum([sympy.isprime(d) for d in c_diags])
      if (perc := n_diag_primes/(len(spiral[0])*2 - 1)) < 0.10:
        print(len(spiral[0]))
        break

      print(perc)
      n += 2
    except IndexError:
      pa(spiral)
      raise IndexError

pa = lambda A: print('\n'.join([''.join(['{:4}'.format(item) for item in row])\
                  for row in A]))
if __name__ == '__main__':
  import sys ; sys.path.append('..')
  from utils import call
  call(spiral_primes)

