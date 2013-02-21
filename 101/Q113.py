memo = {}
def monocount(d):
  def inc(x, l):
    if l == 1:
      return 9-x+1
    else:
      if (x, l) in memo:
        return memo[(x, l)]
      else:
        v = sum(inc(y, l-1) for y in xrange(x, 10))
        memo[(x, l)] = v
        return v

  def dec(x, l):
    if l == 1:
      return min(9-x+1, 9)
    else:
      if (x, -l) in memo:
        return memo[(x, -l)]
      else:
        v = sum(dec(y, l-1) for y in xrange(x, 10))
        memo[(x, -l)] = v
        return v

  return inc(1, d) + dec(0, d) - 9

c = 0
for d in xrange(1, 100+1):
  c += monocount(d)
print c
