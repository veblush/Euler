import sys
import math
import itertools

# ready prime array
primes = [2]
for i in xrange(3, 1000000):
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

pset = set(primes)
for p in primes:
  if p < 10:
    continue
  s = [int(c) for c in str(p)]
  for ds in xrange(1, len(s)):
    for rp in itertools.combinations(range(len(s)), ds):
      cc = []
      for i in xrange(10):
        if i == 0 and 0 in rp:
          continue
        k = s[:]
        for j in rp:
          k[j] = i
        iv = sum(10**(len(k)-d-1) * x for d, x in enumerate(k))
        if iv in pset:
          cc.append(iv)
      if len(cc) == 8:
        print sorted(cc)
        sys.exit()
