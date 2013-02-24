import itertools

a = 15
s = 0
for i in xrange(0, (a+1)/2):
  if i == 0:
    b = 1
  else:
    b = 0
    for x in itertools.combinations(range(1, a+1), i):
      b += reduce(lambda x, y: x*y, x)
  s += b

t = reduce(lambda x, y: x*y, range(2, a+2))
print t / s
