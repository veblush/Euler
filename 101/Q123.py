import math

# ready prime array
primes = [2]
for i in xrange(3, 1000000+1):
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

# just get residue from 2
g = lambda p, n: (2*p*n) % (p*p) if n % 2 else 2
for i, p in enumerate(primes, start=1):
  r = g(p, i)
  if r > 10**10:
    print i
    break
