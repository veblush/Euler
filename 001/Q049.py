import math

# ready prime array
primes = [2]
for i in xrange(3, 10000):
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
for i in primes:
  if i < 1000:
    continue
  for j in primes:
    if i >= j:
      continue
    k = j + (j - i)
    if k in pset:
      i_s = sorted(c for c in str(i))
      j_s = sorted(c for c in str(j))
      k_s = sorted(c for c in str(k))
      if i_s == j_s and j_s == k_s:
        print "%d%d%d" % (i, j, k)
