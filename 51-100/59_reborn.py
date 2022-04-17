# 1. UN XOR
# 2. DE-ASCII

tbin = lambda o: "0" * (8 - len(r := bin(o)[2:])) + r

def xor(c, k):
  ret = [''.join([str(int(i != j)) for i, j in zip(u,v)]) for u,v in zip(c, k)]
  s = sum([int(t, 2) for t in ret])
  ret = ''.join([chr(int(t, 2)) for t in ret])
  return (ret, s)

with open("/Users/dude/fun/project_euler/data/p059_cipher.txt") as f:
  data = f.read().split(',')
  data = [tbin(int(d)) for d in data]

def unencrypt():
  cwords = [" is ", " for "]
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  for p in alphabets:
    for q in alphabets:
      for r in alphabets:
        key = [tbin(ord(t)) for t in [p,q,r]]
        key *= (int(len(data)/3))
        unenc, s = xor(key, data)
        if all([w in unenc for w in cwords]):
          print(f'data:\t{unenc}\n key: {p+q+r}\n sum: {s}')
          return 0

unencrypt()
