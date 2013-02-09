from fractions import gcd

c = 0
a, b = 1, 2
for i in xrange(1, 1000):
  a, b = b, a+b*2
  aa = a + b
  if len(str(aa)) > len(str(b)):
    c += 1
print c
