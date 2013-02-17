import math
import itertools

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

def sum_factor(n):
  fs = get_factor(n)
  c = 0 
  for x in itertools.product(*[range(k+1) for p, k in fs]):
    k = reduce(lambda x, y: x*y, [k[0]**x for k, x in zip(fs, x)], 1)
    c += k
  return c - k

M = 1000000

def get_chain(n):
  x = n
  c = 1
  s = set()
  while True:
    x = sum_factor(x)
    if x > M:
      return None
    if x == 1:
      return None
    if n == x:
      s.add(x)
      return s
    if x in s:
      return None
    c += 1
    s.add(x)

m = (0, 0, 0)
for i in xrange(2, M):
  chain = get_chain(i)
  if chain:
    if len(chain) > m[0]:
      m = (len(chain), i, min(chain))
print m
