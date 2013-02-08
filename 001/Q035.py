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
r = 0
for p in primes:
  s = str(p)
  for i in xrange(len(s)-1):
    s = s[1:] + s[0]
    if int(s) not in pset:
      break
  else:
    r += 1
print r
