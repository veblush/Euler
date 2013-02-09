x = 0
for a in xrange(1, 100):
  for b in xrange(1, 100):
    c = a ** b
    s = sum(int(d) for d in str(c))
    x = max(x, s)
print x