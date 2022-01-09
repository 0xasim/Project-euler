import numpy as np

def gen_spiral(dim):
  spiral = np.zeros((dim, dim), dtype=int)
  for n, s in zip(range(dim, 0, -1), range(dim, 0, -2)):
    spiral[dim-n, np.arange(dim-n,n)] = np.arange(s**2 - s + 1, s**2 + 1)
    spiral[np.arange(dim-n,n),dim-n] = np.arange(spiral[dim-n,dim-n],\
                                          spiral[dim-n,dim-n] - s, -1)
    spiral[n-1, np.arange(dim-n,n)] = np.arange(spiral[n-1,dim-n],\
                                          spiral[n-1,dim-n] - s, -1)
    spiral[np.arange(dim-n+1, n),n-1] = np.arange(spiral[n-1,n-1] \
                                            - s + 2, spiral[n-1,n-1] + 1)
  print(spiral, spiral.shape)
  return spiral

spiral = gen_spiral(10) 
print(sum([spiral[i,i]+spiral[spiral.shape[0]-i-1, i] for i in range(spiral.shape[0])])-1)
