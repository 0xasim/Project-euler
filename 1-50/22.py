with open('names.txt', 'r') as f:
  data = f.read()
names = sorted(data.replace('"','').split(','))
alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]
av = {a : i for i, a in zip(range(1, len(alphabets)+1), alphabets)}
worth = lambda name: sum([av[l] for l in name])
print(sum([worth(name)*(i+1) for i, name in enumerate(names)]))
