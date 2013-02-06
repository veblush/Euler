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

# get factor count by primes
def get_factor_count(n):
  c = 1
  for p in primes:
    if n % p == 0:
      k = 1
      m = n / p
      while True:
        if m % p != 0:
          break
        m /= p
        k += 1
      c *= (k+1)
  return c

def run(n):
  s = 0
  i = 1
  while True:
    s += i
    i += 1
    if get_factor_count(s) > n:
      return s

print run(5)
print run(500)

