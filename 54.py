kinds = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # 14 kinds
suits = 'CDHS'  # 4 Suits
revKind = dict((k, 0) for k in kinds)

from collections import Counter
def rank_a_hand(hand, h0, h1):
  sh0, sh1 = sorted(h0), sorted(h1)
  sh0C = Counter(sh0)
  three =  [i for i in sh0C if sh0C[i] == 3]
  pairs =  [i for i in sh0C if sh0C[i] == 2]
  # 22, Royal flush       | 0 |
  if sh0 == sorted(kinds):
    return [22]
  # 21, Straight flush    | 0 |
  if all([o.isnumeric() for o in sh0]) and int(sh0[-1]) == int(sh0[0]) + 4\
      and any([all([p == q for p in sh1]) for q in suits]):
    return [21]
  # 20, Four of a kind    | 0 |
  if any([len(sk := [s for s in sh0 if s == c]) == 4 for c in kinds]):
    return [20, sk[0]]
  # 19, Full House        | 2 |  globally max max != value of pair of 3
  if any(three) and any(pairs):
    return [19, [three, pairs]]
  # 18, Flush             | 2 | should resolve fine with highCardV
  if any([len([1 for m in sh1 if m == x]) == 5 for x in suits]):
    return [18]
  # 17, Straight          | 32 | all ints so max(), or highCardV() are same
  if all([o.isnumeric() for o in sh0]) and int(sh0[-1]) == int(sh0[0]) + 4:
    return [17, max(sh0)]
  # 16, Three of a kind   | 33 | max in a 3item pair != globally max
  if any(three):
    return [16, highV(three)]
  # 15, Two Pairs         | 101 | max value != max value in pairs
  if len(pairs) == 2:
    return [15, highV(pairs)]
  # 14, One Pair          | 825 | should do as pair value comparison is done
  elif len(pairs) == 1:
    return [14, highV(pairs)]
  # 0-13, highest card    | 482 + 362 + 287 + 190 + 148 + 119 + 88 + 68 + 69 + 68 + 64 + ...
  return [highV(sh0)]

def highV(h0):
  if type(h0) != list: h0 = list(h0)
  return [l[0] for l in enumerate(kinds) if l[1] in h0][-1]
print(highV(['5','3']) > highV(['J', 'Q']))

import numpy as np
def highCardV(p1h0, p2h0):
  for k in kinds:
    p1i, p1 = [k for k in enumerate(kinds) if k[1] in p1h0][-1]
    p2i, p2 = [k for k in enumerate(kinds) if k[1] in p2h0][-1]
    if p1 == p2:
      p1h0.remove(p1)
      p2h0.remove(p2)
      continue
    return np.where(p1i > p2i, 1, 2)

def winner(play): 
  global p1_wins, p2_wins
  assert len(play) == 10
  p1h, p2h = play[:5], play[5:]
  p1h0, p1h1 = [c[0] if c[0] != 'T' else '10' for c in p1h], [c[1] for c in p1h]
  p2h0, p2h1 = [c[0] if c[0] != 'T' else '10' for c in p2h], [c[1] for c in p2h]

  r1 = rank_a_hand(p1h, p1h0, p1h1)
  r2 = rank_a_hand(p2h, p2h0, p2h1)
  print(r1, r2, end =' ')
  if r1 > r2: return 1
  elif r2 > r1: return 2
  return highCardV(p1h0[:], p2h0[:])

def euler_54(fname):
  p1_wins, p2_wins = 0, 0
  with open(fname) as f:
    poker_hands = f.read().split('\n')[:-1]
    poker_hands = [p.split() for p in poker_hands]

  for h in poker_hands:
    won = winner(h)
    if won == 1: p1_wins += 1
    else: p2_wins += 1
    print(won)
  return (f'p1_wins: {p1_wins}, p2_wins:{p2_wins}')

print(euler_54('data/p054_poker.txt'))
# print(euler_54('data/p054_poker_test.txt'))


