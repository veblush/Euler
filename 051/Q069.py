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

# get factor by primes
def get_factor(n):
  nn = int(math.sqrt(n))
  f = []
  for p in primes:
    if p > nn:
      break
    if n % p == 0:
      f.append(p)
  return f

m = (0, 0)
for i in xrange(2, 1000000):
  f = get_factor(i)
  phi = reduce(lambda x, p: x * (p-1) / p, f, i)
  v = float(i) / phi
  if v > m[0]:
    m = (v, i)
print m[1]
