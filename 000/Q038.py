m = []
for i in xrange(1, 100000):
  s = ""
  for j in xrange(1, 10):
    s += str(i * j)
    if len(s) >= 9:
      break
  if len(s) == 9:
    se = set(c for c in s)
    if len(se) == 9 and '0' not in se:
      m.append(s)
print sorted(m)[-1]
