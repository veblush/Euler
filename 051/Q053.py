import math

ncr = lambda n, r: math.factorial(n) / math.factorial(r) / math.factorial(n-r)

x = 0
for n in xrange(1, 100+1):
  for r in xrange(1, n+1):
    if ncr(n, r) > 1000000:
      x += 1
print x
