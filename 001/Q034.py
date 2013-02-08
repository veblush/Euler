import math

d = (1, ) + tuple(math.factorial(n) for n in xrange(1, 10))
v = []
for i in xrange(3, 1000000):
  s = sum(d[ord(c) - ord('0')] for c in str(i))
  if s == i:
    v.append(i)

print sum(v), v
