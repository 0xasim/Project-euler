import itertools

def has_cube_root(d):
  cube_root = round(d ** (1/3))
  is_root = cube_root ** 3 == d
  return is_root

def permute_number(n_cube):
  n_cube_list = [int(v) for v in str(n_cube)]
  print('done cube list')
  n_cube_perms = itertools.permutations(n_cube_list)
  print('done itertools.permutations')
  # n_cube_perms = set(list(n_cube_perms))
  print('done set(list')
  # sets to numbers
  n_cube_perms = [int(''.join(map(str, d))) for d in n_cube_perms if d[0] != 0]
  print('done sets to numbers')
  # n_cubic_perms = [sum(d * 10**i for i, d in enumerate(f[::-1])) for f in n_cube_perms]
  return n_cube_perms

def permute_number_better(n_cube):
  n_cube_perms = itertools.permutations(str(n_cube))
  print(list(n_cube_perms))

def run_process(start, finish, nth):
  n = start
  while n < finish:
    print(n)
    n_cube = n ** 3
    print('done cube')
    n_cube_perms = permute_number_better(n_cube)
    print('done perms')
    n_cube_roots = [has_cube_root(d) for d in n_cube_perms]
    print('done cube roots')

    if sum(n_cube_roots) == nth:
      cubic_perms = list(itertools.compress(n_cube_perms, n_cube_roots))
      print("found "*10)
      print(f'{len(cubic_perms)} {n} {cubic_perms}')
      break
    n += 1
  print(start, finish, 'finished'*10)

if __name__ == '__main__':
  from time import time
  from multiprocessing import Process
  S = time()
  nth = 5
  '''
  p1 = Process(target=run_process, args=(0, 1500, nth,))
  p1.start()

  p2 = Process(target=run_process, args=(1500, 1800, nth,))
  p2.start()

  p3 = Process(target=run_process, args=(1800, 2000, nth,))
  p3.start()
  print(f'{time()-S} sec')
  '''
  run_process(5000, 6000, nth)
