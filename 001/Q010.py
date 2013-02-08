import math

primes = []
def is_prime(n):
  x = int(math.sqrt(n))
  for p in primes:
    if n % p == 0:
      return False
    if p > x:
      break
  return True

def run(n):
  primes[:] = []
  for i in xrange(2, n):
    if is_prime(i):
      primes.append(i)
  return sum(primes)

print run(10)
print run(2000000)
