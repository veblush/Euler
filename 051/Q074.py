import math

ds = lambda n: sum(math.factorial(int(c)) for c in str(n))

def f(n):
  ks = set([n])
  i = n
  while True:
    s = ds(i)
    if s in ks:
      return len(ks)
    else:
      ks.add(s)
      i = s

r = []
for i in xrange(1, 1000000):
  v = f(i)
  if v == 60:
    r.append(i)
print len(r), r
