def M(a):
  r = 0
  m = a**2
  i = (a-1) % m
  j = (a+1) % m
  for n in xrange(a*2):
    i = i * (a-1) % m
    j = j * (a+1) % m
    r = max(r, (i + j) % m)
  return r

print sum(M(x) for x in xrange(3, 1000+1))
