import itertools

import sympy
def hasCubeRoot(ep):
  return (type(sympy.root(ep, 3)) == sympy.core.numbers.Integer)

if __name__ == '__main__':
  n = 2
  while True:
    cube = n**3
    cube_s = str(cube)
    cube_perms = itertools.permutations(cube_s)
    cube_perms = [int(str.join('', ep)) for ep in cube_perms]
    has_cubes = [hasCubeRoot(ep) for ep in cube_perms]
    s = sum(has_cubes)/2
    # print(n, len(cube_perms), s)
    if s == 3:
      print(n, cube_perms)
      print(list(itertools.compress(cube_perms, has_cubes)))
      break
    # print(cube_perms, len(cube_perms))
    n += 1

