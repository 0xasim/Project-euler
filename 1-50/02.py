def even_fibonacci(limit):
  even_valued = []
  fibonacci = [1, 2]
  while (fibonacci[-1] < limit):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
  return sum([e for e in fibonacci if e%2 == 0])

if __name__ == "__main__":
  limit = 4000000
  r = even_fibonacci(limit)
  print(r)
