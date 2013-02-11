import sys

d = {}
for i in xrange(1, 10000):
  k = "".join(sorted(str(i ** 3)))
  d.setdefault(k, []).append(i)

for k, v in sorted(d.iteritems(), key=lambda x: x[1][-1]):
  if len(v) >= 5:
    print v[0]**3, v
    sys.exit()
