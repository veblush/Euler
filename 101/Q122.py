mm = {}
def f(n):
  if n == 1:
    return (0, [set((1, ))])
  else:
    if n in mm:
      return mm[n]
    else:
      m = (1000, None)
      for i in xrange(1, n/2+1):
        a, a_ = f(i)
        b, b_ = f(n-i)
        for aa_ in a_:
          for bb_ in b_:
            c_ = set(aa_) & set(bb_)
            c = len(c_)
            d_ = set(aa_) | set(bb_) | set((n, ))
            d = a + b - (c - 1)+ 1
            if d < m[0]:
              m = (d, [d_])
            elif d == m[0]:
              m[1].append(d_)
      mm[n] = m
    return m

M = 200
s = [f(i)[0] for i in xrange(1, M+1)]
print sum(s)
