import math

def pytha(x, y):
  zz = x*x + y*y
  z = int(math.sqrt(zz))
  return z*z == zz

r = 0
for a in xrange(1, 10000):
  for b in xrange(1, a+1):
    for c in xrange(1, b+1):
      if pytha(a, b+c):
        r += 1
  if r > 1000000:
    print a, r
    break
