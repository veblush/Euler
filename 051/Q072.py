import math

# ready prime array
primes = [2]
for i in xrange(3, 1000000+1):
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
      return [n]
    if n % p == 0:
      k = 1
      m = n / p
      while True:
        if m % p != 0:
          break
        m /= p
        k += 1
      return [p] + get_factor(m)

c = 0
for i in xrange(2, 1000000+1):
  f = get_factor(i)
  phi = reduce(lambda x, p: x * (p-1) / p, f, i)
  c += phi
print c
