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

def is_prime(n):
  nn = int(math.sqrt(n))
  for p in primes:
    if p > nn:
      break
    if n % p == 0:
      return False
  return True

ps = set()
for i in xrange(1, 1000):
  for j in xrange(1, i):
    d = i**3 - j**3
    if is_prime(d) and d < 1000000:
      ps.add(d)
print len(ps)
