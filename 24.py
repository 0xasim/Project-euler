from utils import *

# Heap's Algorithm for generating all possible permutations
def lexicograph(o, f='generate'):
  permutations = list()
  def generate(k: int, A: list):
    if k == 1: permutations.append(''.join(A))
    else:
      for i in range(k):
        generate(k-1, A)
        if k % 2 == 0:
          A[i], A[k-1] = A[k-1], A[i]
        else: A[0], A[k-1] = A[k-1], A[0]

  def generate2(k: int, A: list):
    if k == 1: permutations.append(''.join(A))
    else:
      generate2(k-1, A)
      for i in range(k-1):
        if k % 2 == 0:
          A[i], A[k-1] = A[k-1], A[i]
        else: A[0], A[k-1] = A[k-1], A[0]
        generate2(k-1, A)

  eval(f'{f}(len(o), list(o))')
  return (permutations)

seq = '0123456789'
print(lexicograph(seq)[10**6-1])
