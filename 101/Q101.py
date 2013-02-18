from numpy import *

ys = [1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10 for n in xrange(1, 11)]
#ys = [ 1, 8, 27, 64 ]

ti = lambda x: int(x+0.001) if x >= 0 else int(x-0.001)

s = 0
for i in xrange(len(ys)):
  mat = matrix([[(x+1)**(i-t) for t in range(i+1)] for x in range(0, i+1)])
  ces = array([ti(a) for a in (mat.getI() * array(ys[:i+1]).reshape(i+1, 1)).getA().reshape(i+1)])
  k = int(sum([((i+1)+1)**(i-t) for t in range(i+1)] * ces))
  s += k
print s
