import math

# ready prime array
primes = [2]
for i in xrange(3, 100000000):
  ii = int(math.sqrt(i))
  composite = False
  for p in primes:
    if p > ii:
      break
    if i % p == 0:
      composite = True
      break
  if not composite:
    primes.append(i)

# make pairs making a prime sequence
ts = {}
tp = set()
pset = set(primes)
for p in primes:
  s = str(p)
  for i in xrange(1, len(s)):
    if s[i] == '0':
      continue
    p0 = int(s[:i])
    p1 = int(s[i:])
    px = int(str(p1) + str(p0))
    if p0 in pset and p1 in pset and px in pset:
      ts.setdefault(min(p0, p1), set()).add(max(p0, p1))
      ts.setdefault(max(p0, p1), set()).add(min(p0, p1))
      tp.add((min(p0, p1), max(p0, p1)))

# grow set
left = list(tp)
while len(left) > 0:
  x = left.pop()
  newly = set()
  ss = reduce(set.intersection, (ts[xx] for xx in x))
  for s in ss:
    if not all(s in ts[xx] for xx in x if s != x):
      continue
    nn = tuple(sorted(list(x) + [s]))
    if nn not in tp and nn not in newly:
      newly.add(nn)
  for n in newly:
    if n not in tp:
      if len(n) >= 5:
        print sum(n), n
      tp.add(n)
      left.append(n)
