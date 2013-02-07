import math

def get_factors(n):
  r = [1]
  nn = int(math.sqrt(n))
  for i in xrange(2, nn+1):
    if n % i == 0:
      r.append(i)
      if i != n/i:
        r.append(n / i)
  return r

an = []
for i in xrange(1, 28123):
  sd = sum(get_factors(i))
  if sd > i:
    an.append(i)

v = set(xrange(1, 28123))
for i in an:
  for j in an:
    v.discard(i+j)
print sum(v)
