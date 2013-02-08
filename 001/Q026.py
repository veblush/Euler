def run(d):
  x = 1
  r = []
  while True:
    if x < d:
      c = 0
    else:
      c = x / d
      x = x % d
    if (x, c) in r:
      i = r.index((x, c))
      return "".join(str(c) for x, c in r[i:])
      break
    r.append((x, c))
    x *= 10
    if x == 0:
      return ""

cycle_max = (0, "")
for i in xrange(1, 1000):
  cycle = run(i)
  if len(cycle) > len(cycle_max[1]):
    cycle_max = (i, cycle)
print cycle_max
