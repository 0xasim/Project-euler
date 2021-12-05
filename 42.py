from itertools import count
# p042_words.txt
with open('data/p042_words.txt') as f:
  words = list((f.read()).replace('"','').split(','))
alph = dict(zip([chr(i) for i in range(ord('A'), ord('Z') + 1)], count(1)))
wValue = lambda w: sum([alph[l] for l in w])
triWords = lambda stop: {int(eval('n*(n+1)/2')) for n in range(1, stop + 1)}
fewTw = triWords(10**3)
print(len([wv for ew in words if (wv := wValue(ew)) in fewTw]))

