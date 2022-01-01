
dshire = __import__('54_dreamshire')
kinds = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # 13 kinds
suits = 'CDHS'  # 4 Suits
revKind = dict((k, 0) for k in kinds)

from collections import Counter
def rank_a_hand(h0, h1):
  h0C, h1C = Counter(h0), Counter(h1)
  pairs, three, fours = [[i for i in h0C if h0C[i] == j] for j in range(2, 5)]
  consec = all([o.isnumeric() for o in h0]) and not any([True for i in h0C if h0C[i] > 1])\
      and (sh0 := [str(j) for j in sorted([int(i) for i in h0])])\
      and int(sh0[-1]) == int(sh0[0]) + 4
  print(h0C, h0, consec, not any([True for i in h0C if h0C[i] > 1]))
  sameSuit = [h1C[i] for i in h1C if h1C[i] == 5]

  # 22, Royal flush       | 1 |
  if set(['A','K','Q','J','10']) == set(h0):
    return [22]
  # 21, Straight flush    | 0 |
  if any(sameSuit) and consec:
    return [21]
  # 20, Four of a kind    | 0 |
  if any(fours):
    return [20, highV(fours)]
  # 19, Full House        | 2 |
  if any(three) and any(pairs):
    return [19, [highV(three), highV(pairs)]]
  # 18, Flush             | 2 |
  if any(sameSuit):
    return [18]
  # 17, Straight          | 32 |
  if consec:
    return [17]
  # 16, Three of a kind   | 33 |
  if any(three):
    return [16, highV(three)]
  # 15, Two Pairs         | 101 |
  if len(pairs) == 2:
    # print(pairs)
    return [15, highV(pairs)]
  # 14, One Pair          | 825 |
  if len(pairs) == 1:
    return [14, highV(pairs)]
  # 0-12, highest card    | 482 + 362 + 287 + 190 + 148 + 119 + 88 + 68 + 69 + 68 + 64 + ...
  return [highV(h0)[0], highV(h0)[1:]]

highV = lambda h0: [l[0] for l in enumerate(kinds) if l[1] in h0][::-1]
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

def winner(p1, p2): 
  r1 = rank_a_hand(p1[0], p1[1])
  r2 = rank_a_hand(p2[0], p2[1])
  print(r1, r2, end ='\n')
  if r1 > r2: return 1
  elif r2 > r1: return 2
  print('comparing high '*5)
  return highCardV(p1[0], p2[0])

dshire_winner = lambda play: np.where(dshire.hand_rank(play[:5]) >\
    dshire.hand_rank(play[5:]), 1, 2)

def euler_54(fname):
  p1_wins, p2_wins = 0, 0
  p1_ds_wins, p2_ds_wins = 0,0
  with open(fname) as f:
    poker_hands = f.read().split('\n')[:-1]
    poker_hands = [p.split() for p in poker_hands]

  for pI, play in enumerate(poker_hands):
    assert len(play) == 10
    p1h, p2h = play[:5], play[5:]
    p1 = [c[0] if c[0] != 'T' else '10' for c in p1h], [c[1] for c in p1h]
    p2 = [c[0] if c[0] != 'T' else '10' for c in p2h], [c[1] for c in p2h]
    my_winner = winner(p1, p2)
    # print(my_winner)
    ds_winner = dshire_winner(play)
    print(my_winner, ds_winner, pI+1)
    assert my_winner == ds_winner

euler_54('data/p054_poker.txt')
# euler_54('data/p054_poker_test.txt')


