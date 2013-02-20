ds = [(x*2, 'D' + str(x)) for x in xrange(1, 21)] + [(50, 'DB')]
ts = [(x*3, 'T' + str(x)) for x in xrange(1, 21)]
ss = [(x*1, 'S' + str(x)) for x in xrange(1, 21)] + ds + ts + [(25, 'B')]

def f(N):
  def g(n, i, r, a):
    for k in xrange(i, len(ss)):
      s = ss[k]
      if s[0] < n:
        if len(r) < 1:
          g(n - s[0], k, r + [s], a)
      elif s[0] == n:
        a.append(r + [s])
  # set the last double dart and get all combinations
  c = 0
  for s in ds:
    n = N - s[0]
    if n > 0:
      a = []
      g(n, 0, [], a)
      c += len(a)
    elif n == 0:
      c += 1
  return c

r = 0
for i in xrange(1, 100):
  r += f(i)
print r
