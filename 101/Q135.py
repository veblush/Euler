import math

# assume that z, y, z = x+2d, x+d, x
# and solve 3d-x=a, d+x=b equation
def f(a, b):
  if (a + b) % 4 != 0:
    return None
  d = (a + b) / 4
  x = b - d
  if x <= 0:
    return None
  return (x, d)

def g(n):
  c = 0
  nn = int(math.sqrt(n))
  for i in xrange(1, nn+1):
    if n % i != 0:
      continue
    j = n / i
    a = f(i, j)
    if a:
      c += 1
    if i != j:
      b = f(j, i)
      if b:
        c += 1
  return c

r = 0
for x in xrange(1, 1000000):
  if g(x) == 10:
    r += 1
print r
