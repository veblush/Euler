def run(n):
  s = 0
  for i in xrange(1, n):
    if i % 3 == 0 or i % 5 == 0:
      s += i
  return s

print run(10)
print run(1000)
