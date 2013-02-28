# covering xy plane
def f(size):
  s = size[0] * 2 + size[1] * 2
  yield s
  while True:
    s = s + 4
    yield s

# covering z with xy planes
def g(size):
  y = [size[0]*size[1]]
  for s in f(size):
    v = s*size[2] + sum(y)*2
    y.insert(0, s)
    yield v

# scan all possible cases
q = {}
m = 10000
M = 20000
for x in xrange(1, m):
  for y in xrange(x, m):
    if g((x, y, 1)).next() > M:
      break
    for z in xrange(y, m):
      for i, v in enumerate(g((x, y, z))):
        if v > M:
          break
        q.setdefault(v, 0)
        q[v] += 1
      if i == 0:
        break
print sorted(filter(lambda x: x[1] == 1000, q.iteritems()))[0][0]
