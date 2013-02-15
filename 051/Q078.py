# by partitioning generate function

pn = lambda n: (3*n*n - n)/2

l = 1000000
s = [1]
for n in xrange(1, l):
  p = 0
  for m in xrange(1, n+1):
    c = 1 if (m % 2) == 1 else -1
    k1 = n - pn(m)
    k2 = n - pn(m) - m
    p += c * (s[k1] if k1 >= 0 else 0)
    p += c * (s[k2] if k2 >= 0 else 0)
    if k2 < 0:
      break
  s.append(p)
  if p % 1000000 == 0:
    print n
    break
