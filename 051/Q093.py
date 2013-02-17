import itertools

def f(a):
  if len(a) == 1:
    q = int(a[0])
    return [q] if a[0] == q and q > 0 else []
  r = []
  for i in xrange(len(a)-1):
    r.extend(f(a[:i] + [a[i] + a[i+1]] + a[i+2:]))
    r.extend(f(a[:i] + [a[i] - a[i+1]] + a[i+2:]))
    r.extend(f(a[:i] + [a[i] * a[i+1]] + a[i+2:]))
    if a[i+1] != 0:
      r.extend(f(a[:i] + [a[i] / float(a[i+1])] + a[i+2:]))
  return r

def g(a):
  r = set()
  for x in itertools.permutations(a):
    r |= set(f(list(x)))
  return sorted(r)

def longest(a):
  for i, v in enumerate(a):
    if i != v-1:
      return i
  return len(a)

m = (0, 0)
for a in itertools.combinations(range(1, 10), 4):
  l = longest(g(a))
  if l > m[0]:
    m = (l, a)
print m
