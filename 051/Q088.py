M = 12000
k = [0]*(M+1)

def f(n, d, a):
  for i in xrange(2, n+1):
    c = a[0]*i, a[1] + i, a[2] + 1
    if c[0] > M*2:
      return
    if d > 1:
      f(n, d-1, c)
    else:
      x = c[0] - c[1]
      if x >= 0:
        ki = c[2] + x
        if ki >= 2 and ki < len(k) and (k[ki] == 0 or c[0] < k[ki]):
          k[ki] = c[0]

for d in xrange(2, 20):
  f(M, d, (1, 0, 0))

print sum(set(k[2:]))
