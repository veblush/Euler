import math

def f(n):
  for x in xrange(2, int(math.sqrt(n))+1):
    q = n / x
    r = n % x
    if r * q == x * x: # r, x, q = x, x*k, x*k*k
      return True
  return False

s = 0
for i in xrange(1, int(math.sqrt(10**12))):
  n = i * i
  if f(n):
    s += n
print s
