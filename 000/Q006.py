def run(n):
  s = 0
  for a in xrange(1, n+1):
    for b in xrange(1, n+1):
      if a != b:
        s += a*b
  return s

print run(10)
print run(100)
