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

def is_prime(n):
  nn = int(math.sqrt(n))
  for p in primes:
    if p > nn:
      break
    if n % p == 0:
      return False
  return True

# through iterating all run number check prime
n = 10
s = 0
for d in xrange(0, 10):
  pcount = 0
  psum = 0
  for m in xrange(n, 0, -1):
    for r in itertools.combinations(range(0 if d > 0 else 1, n), m):
      xs = []
      for i in xrange(n):
        if i in r:
          xs.append(range(d, d+1))
        elif i == 0:
          xs.append(range(1, 10))
        else:
          xs.append(range(0, 10))
      for j in itertools.product(*xs):
        x = sum(v*10**(n-i-1) for i, v in enumerate(j))
        if is_prime(x):
          pcount += 1
          psum += x
    if pcount > 0:
      s += psum
      break
print s
