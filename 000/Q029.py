def run(a, b):
  s = set()
  for i in xrange(2, a+1):
    for j in xrange(2, b+1):
      s.add(i**j)
  return len(s)

print run(5, 5)
print run(100, 100)
