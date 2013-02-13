from fractions import gcd

m = (0, 0, 0)
for i in xrange(1, 1000000+1):
  x = i*3 / 7
  y = float(x) / i
  if y > m[0]:
    d = gcd(x, i)
    v0 = x / d
    v1 = i / d
    if v1 != 7:
      m = (y, x, i)
print m[1]
