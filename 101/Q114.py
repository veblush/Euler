def f(n):
  memo_r = {}
  def r(n):
    if n < 3:
      return 0
    else:
      if n in memo_r:
        return memo_r[n]
      else:
        v = 1 + sum(b(x) for x in xrange(1, n-2))
        memo_r[n] = v
        return v
  memo_b = {}
  def b(n):
    if n < 3:
      return 1
    else:
      if n in memo_b:
        return memo_b[n]
      else:
        v = 1 + sum(r(x) for x in xrange(3, n))
        memo_b[n] = v
        return v
  return r(n) + b(n)

print f(7)
print f(50)
