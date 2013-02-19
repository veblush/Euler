import math
import itertools

# ready prime array
primes = [2]
for i in xrange(3, 100000+1):
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
  if n == 1:
    return []
  nn = int(math.sqrt(n))
  for p in primes:
    if p > nn:
      return [(n, 1)]
    if n % p == 0:
      k = 1
      m = n / p
      while True:
        if m % p != 0:
          break
        m /= p
        k += 1
      return [(p, k)] + get_factor(m)

for n in xrange(2, 100000000):
  pis = [[p**i for i in xrange(k*2+1)] for p, k in get_factor(n)]
  s = set()
  for xs in itertools.product(*pis):
    v = reduce(lambda x, y: x*y, xs)
    s.add(v)
  r = (len(s) / 2) + (len(s) % 2)
  if r > 1000:
    print n, r
    break
