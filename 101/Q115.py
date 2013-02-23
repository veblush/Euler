m = 3

def f(n):
  memo_r = {}
  def r(n):
    if n < m:
      return 0
    else:
      if n in memo_r:
        return memo_r[n]
      else:
        v = 1 + sum(b(x) for x in xrange(1, n-m+1))
        memo_r[n] = v
        return v
  memo_b = {}
  def b(n):
    if n < m:
      return 1
    else:
      if n in memo_b:
        return memo_b[n]
      else:
        v = 1 + sum(r(x) for x in xrange(m, n))
        memo_b[n] = v
        return v
  return r(n) + b(n)

m = 50
for i in xrange(50, 1000):
  if f(i) > 1000000:
    print i
    break
