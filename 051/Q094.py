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
M = 1000000000
for x in xrange(2, M/3):
  a = 3*x*x + 2*x - 1
  b = check(a)
  if b != 0 and ((x-1)*b) % 2 == 0:
    s += 3*x-1
  a = 3*x*x - 2*x - 1
  b = check(a)
  if b != 0 and ((x+1)*b) % 2 == 0:
    s += 3*x+1
print s
