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

# check
pset = set(primes)
r = []
for p in primes:
  if p < 10:
    continue
  s = str(p)
  for i in xrange(len(s)-1):
    if int(s[i+1:]) not in pset:
      break
    if int(s[:i+1]) not in pset:
      break
  else:
    r.append(p)
print sum(r), r
