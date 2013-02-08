import sys
import math
import itertools

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
    if n % p == 0:
      return False
    if p > nn:
      break
  return True

for d in xrange(9, 0, -1):
  for vv in itertools.permutations(xrange(d, 0, -1)):
    v = sum(10**(d - i - 1) * k for i, k in enumerate(vv))
    if is_prime(v):
      print v
      sys.exit()
