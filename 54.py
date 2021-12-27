with open('data/p054_poker.txt') as f:
  poker_hands = f.read().split('\n')[:-1]
  poker_hands = [p.split() for p in poker_hands]

def rank_a_hand(hand):
  h0, h1 = [c[0] for c in hand], [c[1] for c in hand]
  if all([o.isnumeric() for o in h0]) and int(sorted(h0)[-1]) == int(sorted(h0)[0])+ 4:
    print('Straight Flush:2')

def winner(play): 
  assert len(play) == 10
  p1h = play[:5]
  p2h = play[5:]
  rank_a_hand(p1h)
  rank_a_hand(p2h)

for h in poker_hands:
  winner(h)
