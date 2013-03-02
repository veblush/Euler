import math

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

def f(n):
  if n % 2 == 0 or n % 5 == 0:
    return None
  a, d = 1, 1
  while True:
    a = a % n
    if a == 0:
      return d
    a = a * 10 + 1
    d += 1

s = 0
for p in primes:
  r = f(p)
  if not r or any(n not in (2, 5) for n, k in get_factor(r)):
    s += p
print s
