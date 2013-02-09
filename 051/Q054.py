from collections import Counter

def rank(cs):
  cc = sorted([c[0] for c in cs])
  cm = dict(Counter(cc))
  im = dict()
  for k, v in cm.iteritems():
    im.setdefault(v, []).append(k)
  for k, v in im.iteritems():
    im[k] = tuple(sorted(im[k], reverse=True))
  is_same_suit = all(cs[x][1] == cs[0][1] for x in xrange(1, 5))
  
  # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
  if is_same_suit and cc == [10, 11, 12, 13, 14]:
    return 9000
  # Straight Flush: All cards are consecutive values of same suit.
  if is_same_suit:
    if cc == [cc[0], cc[0]+1, cc[0]+2, cc[0]+3, cc[0]+4]:
      return 8000 + cc[0]
  # Four of a Kind: Four cards of the same value.
  if len(cm) == 2:
    if cm[cc[0]] == 4:
      return 7000 + cc[0]
    if cm[cc[-1]] == 4:
      return 7000 + cc[-1]
  # Full House: Three of a kind and a pair.
  if len(cm) == 2:
    if cm[cc[0]] == 3:
      return 6000 + cc[0]
    if cm[cc[-1]] == 3:
      return 6000 + cc[-1]
  # Flush: All cards of the same suit.
  if is_same_suit:
    return 5000
  # Straight: All cards are consecutive values.
  if cc == [cc[0], cc[0]+1, cc[0]+2, cc[0]+3, cc[0]+4]:
    return 4000 + cc[0]
  # Three of a Kind: Three cards of the same value.
  if 3 in im:
    return 3000 + im[3][0]
  # Two Pairs: Two different pairs.
  if 2 in im and len(im[2]) == 2:
    return 2000 + im[2][0] * 20 + im[2][1]
  # One Pair: Two cards of the same value.
  if 2 in im and len(im[2]) == 1:
    return 1000 + im[2][0]
  return 0

def who_win(cl, cr):
  rl, lr = rank(cl), rank(cr)
  if rl > lr:
    return -1
  elif rl < lr:
    return 1
  else:
    hl = tuple(sorted([c[0] for c in cl], reverse=True))
    hr = tuple(sorted([c[0] for c in cr], reverse=True))
    if hl > hr:
      return -1
    elif hl < hr:
      return 1
    else:
      return 0

co = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
r = 0
for line in open("Q054_poker.txt"):
  cs = line.strip().split()
  if len(cs) == 10:
    cs_a= [(c[0], c[1]) for c in cs]
    for i in xrange(len(cs_a)):
      cs_a[i] = (co.index(cs_a[i][0]), cs_a[i][1])
    ww = who_win(cs_a[:5], cs_a[5:])
    if ww == -1:
      r += 1
print r
