import math

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

x = []
for i in xrange(1, 100000+1):
  fs = get_factor(i)
  rad = reduce(lambda x, y: x*y[0], fs, 1)
  x.append((rad, i))
print sorted(x)[10000-1][1]
