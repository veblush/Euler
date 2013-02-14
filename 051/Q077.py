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
pset = set(primes)

# with intermediate function
n = 100
a = [[0] * (n+1) for x in xrange(n+1)]
for i in xrange(1, n+1):
  a[i][i] = 1 if i in pset else 0
  for k in xrange(i-1, 0, -1):
    a[i][k] = a[i][k+1] + (a[i-k][k] if k in pset else 0)
  if a[i][1] > 5000:
    print i
    break
