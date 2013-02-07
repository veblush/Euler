import math

def is_not_prime(n):
  if n <= 1:
    return True
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return True
  return False

def get_max_primes(a, b):
  n = 0
  while True:
    x = n*n + a*n + b
    if is_not_prime(x):
      return n - 1
    n += 1

m = (0, 0, 0)
for a in xrange(-999, 1000):
  for b in xrange(-999, 1000):
    v = get_max_primes(a, b)
    if v > m[2]:
      m = (a, b, v)
print m, m[0]*m[1]
