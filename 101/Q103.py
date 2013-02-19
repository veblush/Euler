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

for n in xrange(2, 7+1):
  ms = (1000, 0)
  for k in xrange(1, n*n):
    for c in itertools.combinations(range(1, k), (n-1)):
      x = c + (k,)
      if sss(x):
        if sum(x) < ms[0]:
          ms = (sum(x), x)
  print n, ":", "".join(str(i) for i in ms[1])
