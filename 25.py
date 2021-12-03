def fib_num_dig_index(n):
  l1, l2 = (1, 1)
  i = 2
  while True:
    l2, l1 = l1, l1+l2
    i += 1
    if len(str(l1)) == n:
      print(i, l1)
      break
  
fib_num_dig_index(1000)
