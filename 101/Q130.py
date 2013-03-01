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

def is_prime(n):
  nn = int(math.sqrt(n))
  for p in primes:
    if p > nn:
      break
    if n % p == 0:
      return False
  return True

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
c = 0
for n in xrange(2, 100000):
  if is_prime(n):
    continue
  v = f(n)
  if v and (n - 1) % v == 0:
    s += n
    c += 1
    if c == 25:
      break
print s
