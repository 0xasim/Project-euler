d2bin = lambda data: [bin(d)[2:] for d in data]
bin2d = lambda binary: [int(b, 2) for b in binary]
xor = lambda a,b: int(a != b)
toascii = lambda num: [ord(e) for e in num]
unascii = lambda asc: [chr(e) for e in asc]

with open('/Users/dude/fun/project_euler/data/p059_cipher.txt', 'r') as f:
  sdata = f.read().split('\n')[0].split(',')
  data = [int(d) for d in sdata]

def xor_strings(s, t) -> bytes:
    """xor two same length strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

def xor(a, b):
  da = bin(a)[2:];db = bin(b)[2:]
  out = str(); i = 0
  big = da;  smol = db
  if len(da) < len(db):
    big = db;smol = da
  for e in big:
    out += str(int(e ==  smol[i]))
    i += 1
    if i > len(smol)-1: i = 0
  ret = int(out, 2)
  # print(f'{da} < da\n{db} < db\n{out} < out \n ret {ret}')
  return ret

def decrypt(key):
  key = toascii(key)
  i = 0
  xored = list()
  for d in data:
    xored.append(xor(d, key[i]))
    i += 1
    if i > len(key)-1: i=0
  res = ''.join(unascii(xored))
  common_words = [" the ", " and ", " of ", " for ", " is "]
  matched = [1 for ew in common_words if ew in res]
  # resplit = res.split(' ')

  if len(matched) >= 1:
    print("---------------------------------------")
    print(res)
    print("---------------------------------------")

if __name__ == "__main__":
  print(xor(42, 65))
  print(xor(107, 42))
  key = int(''.join([str(v) for v in toascii('abc')]))
  print("key: ", key)
  # print(xor_strings(data, key))

  alph = 'abcdefghijklmnopqrstuvwxyz'
  for a in alph:
    for b in alph:
      for c in alph:
        decrypt(a+b+c)

