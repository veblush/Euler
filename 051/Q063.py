c = 0
for x in xrange(1, 10):
  for y in xrange(1, 30):
    if y == len(str(x**y)):
      c += 1
print c
