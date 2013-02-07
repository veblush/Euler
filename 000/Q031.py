def run(n):
  v = (200, 100, 50, 20, 10, 5, 2, 1)
  def combi(m, i):
    if i < len(v) - 1:
      return sum(combi(m - v[i]*a, i+1) for a in xrange(m / v[i] + 1))
    else:
      return 1
  return combi(n, 0)

print run(200)
