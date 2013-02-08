N = 1000000
g = [
  (n*(n+1)/2 for n in xrange(N)),
  (n*(3*n-1)/2 for n in xrange(N)),
  (n*(2*n-1) for n in xrange(N))]

v = [g[0].next(), g[1].next(), g[2].next()]
while True:
  if v[0] == v[1] and v[1] == v[2] and v[0] > 40755:
    print v[0]
    break
  i = v.index(min(v))
  v[i] = g[i].next()
