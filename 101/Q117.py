def f(n):
  tn = (2, 3, 4)
  mm = {}
  def c(n, t):
    if n < tn[t]:
      return 0
    elif n <= tn[t]+1:
      return 1
    else:
      if (n, t) in mm:
        return mm[(n, t)]
      else:
        v = (b(n-tn[t]) + 
             sum(c(n-tn[t], tt) for tt in range(len(tn))))
        mm[(n, t)] = v
        return v
  def b(n):
    return 1 + sum(sum(c(x, t) for x in xrange(tn[t], n)) for t in range(len(tn)))
  return b(n+1)

print f(5)
print f(50)
