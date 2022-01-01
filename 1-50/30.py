equals_power = lambda n: True if n == sum([int(d)**5 for d in str(n)]) else False
print(sum([n for n in range(10, 10**6) if equals_power(n)]))
