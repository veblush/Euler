import math

def f(n, c):
  x = int(math.sqrt(n))
  a, b = n-x*x, 2*x
  A0, B0 = x, 1
  A1, B1 = b*x + a, b
  for c_ in xrange(c):
    A2, B2 = b*A1 + a*A0, b*B1 + a*B0
    A0, B0 = A1, B1
    A1, B1 = A2, B2
  return A2, B2

r = 0
for n in xrange(1, 100+1):
  nn = int(math.sqrt(n))
  if nn*nn == n:
    continue
  a, b = f(n, 200)
  s = str(a * 10**100 / b)[:100]
  r += sum(int(c) for c in s)
print r
