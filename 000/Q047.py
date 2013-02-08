import math

# ready prime array
primes = [2]
for i in xrange(3, 10000):
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

def get_factors(n):
  f = []
  for p in primes:
    if n % p == 0:
      k = 1
      m = n / p
      while True:
        if m % p != 0:
          break
        m /= p
        k += 1
      f.append((p, k))
  return f

v = [get_factors(i) for i in xrange(1, 5)]
for n in xrange(4, 1000000):
  v[0], v[1], v[2], v[3] = v[1], v[2], v[3], get_factors(n)
  if len(v[0]) == 4 and len(v[1]) == 4 and len(v[2]) == 4 and len(v[3]) == 4:
    print n-3
    break
