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

M = 50000000
r = [0]*M
for i in xrange(1, M):
  for j in xrange(1, (M+i-1)/i):
    if f(i, j):
      r[i*j] += 1
print r.count(1)
