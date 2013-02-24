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
  if n <= 1:
    return False
  nn = int(math.sqrt(n))
  for p in primes:
    if p > nn:
      break
    if n % p == 0:
      return False
  return True

# generate set of the number of subgroups 
# (a1 <= a2 <= ... <= an, a1+a2+..+an == n)
def g(n, m):
  if n < m:
    return
  elif n == m:
    yield [m]
  else:
    for i in range(m, n+1):
      if n-i == 0:
        yield [i]
      else:
        for s in g(n-i, i):
          yield [i, ] + s

def f(n):
  c = [0]
  def ff(a, lg, vs):
    for ds in itertools.permutations(a, lg[0]):
      v = sum(d * 10**(len(ds)-i-1) for i, d in enumerate(ds))
      if len(vs) > 0 and v < vs[-1]:
        continue
      if not is_prime(v):
        continue
      if len(lg) == 1:
        c[0] += 1
      else:
        ff(filter(lambda x: x not in ds, a), lg[1:], vs + [v])
  a = range(1, n+1)
  for lg in g(n, 1):
    ff(a, lg, [])
  return c[0]

print f(9)
