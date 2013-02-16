import math

# ready prime array
primes = [2]
for i in xrange(3, 100000):
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

s = set()
M = 50000000
for p in primes:
  a = p*p
  if a >= M:
    break
  for q in primes:
    b = q*q*q
    if a+b >= M:
      break
    for r in primes:
      c = r*r*r*r
      if a+b+c >= M:
        break
      s.add(a+b+c)
print len(s)
