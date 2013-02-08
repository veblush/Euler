n = [n*(3*n-1)/2 for n in xrange(1, 10000)]
s = set(n)
for a in n:
  for b in n:
    if a < b:
      c = a + b
      d = b - a
      if c in s and d in s:
        print d
