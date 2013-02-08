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

v = 0
for i in xrange(10000):
  sd = sum(get_factors(i))
  if i != sd and i == sum(get_factors(sd)):
    v += i
print v
