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

def is_composite(n):
  nn = int(math.sqrt(n))
  for p in primes:
    if n % p == 0:
      return True
    if p > nn:
      break
  return False

for i in xrange(3, 10000, 2):
  if not is_composite(i):
    continue
  ok = False
  for p in primes:
    if p >= i:
      break
    d = math.sqrt((i - p) / 2)
    if d == int(d):
      ok = True
      break
  if not ok:
    print i
    break
