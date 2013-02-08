from fractions import *

s = []
for i in xrange(11, 100):
  for j in xrange(i+1, 100):
    if i % 10 == j / 10 and j % 10 != 0:
      if Fraction(i, j) == Fraction(i / 10, j % 10):
        s.append((i, j))
    elif i / 10 == j % 10 and i % 10 != 0:
      if Fraction(i, j) == Fraction(i % 10, j / 10):
        s.append((i, j))

v = (1, 1)
for a, b in s:
  v = (v[0] * a, v[1] * b)
print v[1] / gcd(v[0], v[1]), s
