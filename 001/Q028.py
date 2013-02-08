def run(n):
  s = 1
  v = 1
  for i in xrange(1, n+1):
    for q in xrange(4):
      v += 2*i
      s += v
  return s

print run(5/2)
print run(1001/2)
