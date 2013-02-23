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
        v = sum(b(x, t) for x in xrange(n-tn[t], -1, -tn[t]))
        mm[(n, t)] = v
        return v
  def b(n, t):
    return 1 + sum(c(x, t) for x in xrange(tn[t], n))
  return b(n+1, 0) + b(n+1, 1) + b(n+1, 2) - 3

print f(5)
print f(50)
