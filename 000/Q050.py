import math

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
pm = (0, 0)
for i in xrange(0, len(primes)):
  a = primes[i]
  for j in xrange(1, min(len(primes) - i, 1000)):
    a += primes[i + j]
    if a in pset:
      if j > pm[0]:
        pm = (j, a)
print pm
