primes = (2, 3, 5, 7, 11, 13, 17, 19)

def factorize(n):
  r = n
  s = []
  for p in primes:
    c = 0
    while r % p == 0:
      r /= p
      c += 1
    if c > 0:
      s.append((p, c))
  return s

f = {}
for i in xrange(1, 20+1):
  for p, c in factorize(i):
    f[p] = max(f.get(p, 0), c)

r = 1
for p, c in f.iteritems():
  r *= p ** c
print r
