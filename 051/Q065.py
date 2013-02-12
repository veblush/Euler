def f(r):
  h = [ r[0], r[1] * r[0] + 1 ]
  k = [ 1, r[1] ]
  for c in xrange(2, len(r)):
    h.append(r[c] * h[-1] + h[-2])
    k.append(r[c] * k[-1] + k[-2])
  return (h, k)

e = [2]
for i in xrange(1, 40):
  e.append(1)
  e.append(2*i)
  e.append(1)

print sum(int(c) for c in str(f(e)[0][99]))
