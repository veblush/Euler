import itertools

def d(t):
  s = 0
  for i in t:
    s = s * 10 + i
  return s

s = set()
for t in itertools.permutations(range(1, 10)):
  for k in itertools.combinations(range(1, 9), 2):
    a = d(t[:k[0]])
    b = d(t[k[0]:k[1]])
    c = d(t[k[1]:])
    if a * b == c:
      s.add(c)

print sum(s), s
