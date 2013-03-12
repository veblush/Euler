import math
from fractions import gcd

# just enumerate all pythagorean triples
N = 100000000
r = 0
for i in xrange(1, int(math.sqrt(N))):
  for j in xrange(1, i):
    if (i - j) % 2 == 0:
      continue
    if gcd(i, j) != 1:
      continue
    x = i*i - j*j
    y = 2*i*j
    z = i*i + j*j
    p = x + y + z
    if p >= N:
      continue
    if z % abs(x - y) != 0:
      continue
    r = r + N/p
print r

