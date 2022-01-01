divisors = lambda n: [c for c in range(1, int(n/2)+1) if n % c == 0]
isabundant = lambda n: True if sum(divisors(n)) > n else False
abundants = [n for n in range(1, 28123+1) if isabundant(n)]
sumofabun = {i+j for i in abundants for j in abundants}
notinsum = [n for n in range(1, 28123+1) if n not in sumofabun]

print(sum(notinsum))
print(len(sumofabun), len(abundants), len(notinsum))
