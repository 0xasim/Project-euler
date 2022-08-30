ds = dict()
n = 0
nth = 5
while True:
  n_cube = n**3
  n_cube_sorted = int(''.join(sorted(str(n_cube), reverse=True)))
  if not n_cube_sorted in ds:
    ds[n_cube_sorted] = [n]
  else:
    ns = ds[n_cube_sorted]
    ns.append(n)
    if len(ns) == nth:
      print('found'*10)
      print(ns, sorted(ns)[0]**3)
      break
  n += 1
