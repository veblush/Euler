import itertools

def sss(a):
  for i in xrange(1, len(a)-1):
    if sum(a[:i+1]) <= sum(a[-i:]):
      return False
  s = set()
  for i in xrange(1, len(a)):
    for x in itertools.combinations(a, i):
      y = sum(x)
      if y in s:
        return False
      s.add(y)
  return True

r = 0
for line in open("Q105_sets.txt"):
  a = sorted([int(x) for x in line.strip().split(",")])
  if sss(a):
    r += sum(a)
print r
