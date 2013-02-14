from fractions import gcd
import math

limit = 1500000
r = [0]*limit
for i in xrange(1, int(math.sqrt(limit/2))):
  for j in xrange(1, i):
    if (i - j) % 2 == 0:
      continue
    if gcd(i, j) != 1:
      continue
    a = i*i - j*j
    b = 2*i*j
    c = i*i + j*j
    p = a + b + c
    while p < limit:
      r[p] += 1
      p += a + b + c
print r.count(1)
