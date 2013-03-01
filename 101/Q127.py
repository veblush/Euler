import math
import fractions

# ready prime array
primes = [2]
for i in xrange(3, 120000+1):
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

r = 0
for c in xrange(3, 120000):
  cf = get_factor(c)
  if all(k == 1 for (p, k) in cf):
    continue
  for a in xrange(1, c/2+1):
    b = c - a
    if (fractions.gcd(a, b) != 1 or
        fractions.gcd(a, c) != 1 or
        fractions.gcd(b, c) != 1):
      continue
    af = get_factor(a) if a > 1 else [(1, 1)]
    bf = get_factor(b)
    rad_abc = reduce(lambda x, y: x * y[0], af + bf + cf, 1)
    if rad_abc >= c:
      continue
    r += c
print r
