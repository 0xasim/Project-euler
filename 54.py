with open('data/p054_poker_test.txt') as f:
  poker_hands = f.read().split('\n')[:-1]
  poker_hands = [p.split() for p in poker_hands]

kinds = '123456789JQKA' # len(kinds) = 13
suits = 'CDHS'
def rank_a_hand(hand):
  h0, h1 = [c[0] for c in hand], [c[1] for c in hand]
  sh0, sh1 = sorted(h0), sorted(h1)
  # Royal flush | 0 | Not possible because there is no 10
  # ------------------------------------------------
  # Straight flush | 0 
  if all([o.isnumeric() for o in h0]) and int(sh0[-1]) == int(sh0[0]) + 4\
      and any([all([p == q for p in sh1]) for q in suits]):
    return 21
  # Four of a kind | 0
  if any([len([1 for s in sh0 if s == c]) == 4 for c in kinds]):
    return 20
  # Full House | 1
  if any([len([1 for s in sh0 if s == c]) == 3 for c in kinds]) and len(set(sh0)) == 2:
    return 19
  # Flush | 2
  if any([len([1 for m in sh1 if m == x]) == 5 for x in suits]):
    return 18
  # Straight | 31
  if all([o.isnumeric() for o in h0]) and int(sh0[-1]) == int(sh0[0]) + 4:
    return 17
  # Three of a kind | 33 
  if any([len([1 for s in sh0 if s == c]) == 3 for c in kinds]):
    return 16
  # Two of a pair | 80
  if sum([len([1 for s in sh0 if s == c]) == 2 for c in kinds]) == 2:
    return 15
  # Pair | 1171
  if sum([len([1 for s in sh0 if s == c]) == 2 for c in kinds]) == 1:
    return 14
  # High card | | 0-12 values
  return [hcard[0] for hcard in enumerate(kinds) if hcard[1] in sh0][-1]

def winner(play): 
  assert len(play) == 10
  p1h = play[:5]
  p2h = play[5:]
  r1 = rank_a_hand(p1h)
  r2 = rank_a_hand(p2h)
  print(r1, r2, end =' ')
  if r1 > r2: return 1
  elif r2 > r1: return 2
  return "equal"

for h in poker_hands:
  print(winner(h))
