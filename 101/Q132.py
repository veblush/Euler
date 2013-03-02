import math

# ready prime array
primes = [2]
for i in xrange(3, 1000000):
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

k = 10**9
c = 40
s = 0
for p in primes:
  r = f(p)
  if r and k % r == 0:
    s += p
    c -= 1
    if c == 0:
      break
print s
