import math

def check(v):
  if v % 4 != 0:
    return 0
  k = v / 4
  x = int(math.sqrt(k))
  if x*x != k:
    return 0
  return x
 
s = 0
for x in xrange(1, 1000000000+1):
  a = 3*x*x + 2*x - 1
  b = 3*x*x - 2*x - 1
  if check(a) or check(b):
    s += x
print s
