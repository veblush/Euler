from numpy import *

def side(a, b, c):
  return 1 if cross(b - a, c - a) > 0 else -1

c = 0
for line in open("Q102_triangles.txt"):
  p = [int(x) for x in line.strip().split(",")]
  t = [array([p[i*2], p[i*2+1]]) for i in xrange(3)]
  s = [side(t[i], t[(i+1) % 3], array([0, 0])) for i in xrange(3)]
  if len(set(s)) == 1:
    c += 1
print c
