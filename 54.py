
with open('data/p054_poker_test.txt') as f:
  poker_hands = f.read().split('\n')[:-1]
  poker_hands = [p.split() for p in poker_hands]

kinds = '123456789JQKA' # len(kinds) = 13
suits = 'CDHS'
def rank_a_hand(hand, h0, h1):
  sh0, sh1 = sorted(h0), sorted(h1)
  # Royal flush | 0 | Not possible because there is no 10
  # ------------------------------------------------
  # Straight flush | 0 
  if all([o.isnumeric() for o in h0]) and int(sh0[-1]) == int(sh0[0]) + 4\
      and any([all([p == q for p in sh1]) for q in suits]):
    return [21]
  # Four of a kind | 0
  if any([len(sk := [s for s in sh0 if s == c]) == 4 for c in kinds]):
    # print(sk, len(sk))
    return [20, sk[0]]
  # Full House | 1
  if any([len(sk := [s for s in sh0 if s == c]) == 3 for c in kinds]) and len(set(sh0)) == 2:
    # print(sk, len(sk))
    return [19, sk]
  # Flush | 2
  if any([len([1 for m in sh1 if m == x]) == 5 for x in suits]):
    return [18]
  # Straight | 31
  if all([o.isnumeric() for o in h0]) and int(sh0[-1]) == int(sh0[0]) + 4:
    return [17]
  # Three of a kind | 33 
  if any([len([1 for s in sh0 if s == c]) == 3 for c in kinds]):
    return [16]
  # Two Pairs | 80
  if sum([len([1 for s in sh0 if s == c]) == 2 for c in kinds]) == 2:
    return [15]
  # One Pair | 1171
  for c in kinds:
    pv = [s for s in sh0 if s == c]
    if len(pv) == 2:
      return [14, kinds.index(pv[0])]
  # High card | | 0-12 values
  return [[hcard[0] for hcard in enumerate(kinds) if hcard[1] in sh0][-1]]

def highCardV(p1h0, p2h0):
  for k in kinds:
    p1i, p1 = [k for k in enumerate(kinds) if k[1] in p1h0][-1]
    p2i, p2 = [k for k in enumerate(kinds) if k[1] in p2h0][-1]
    if p1i > p2i: return 1
    elif p2i > p1i: return 2
    p1h0.remove(p1)
    p2h0.remove(p2)

def winner(play): 
  assert len(play) == 10
  p1h, p2h = play[:5], play[5:]
  p1h0, p1h1 = [c[0] for c in p1h], [c[1] for c in p1h]
  p2h0, p2h1 = [c[0] for c in p2h], [c[1] for c in p2h]

  r1 = rank_a_hand(p1h, p1h0, p1h1)
  r2 = rank_a_hand(p2h, p2h0, p2h1)
  print(r1, r2, end =' ')
  if r1 > r2: return 1
  elif r2 > r1: return 2
  return highCardV(p1h0[:], p2h0[:])
  return "equal"

for h in poker_hands:
  print(winner(h))

