def f(x, y):
  c = 0
  for a in xrange(1, x+1):
    for b in xrange(1, y+1):
      c += (x-a+1)*(y-b+1)
  return c

s = {}
for x in xrange(1, 100):
  for y in xrange(1, 100):
    s[f(x, y)] = (x, y)

v, r = min(s.iteritems(), key=lambda x: abs(x[0]-2000000))
print v, r, r[0]*r[1]
