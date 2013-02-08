import math
import operator

n = [i*i for i in xrange(1, 1000+1)]
s = set(n)
x = {}
for a in n:
  for b in n:
    if a <= b:
      c = a + b
      if c in n:
        p = int(math.sqrt(a) + math.sqrt(b) + math.sqrt(c))
        if p > 1000:
          continue
        if p in x:
          x[p] += 1
        else:
          x[p] = 1
print max(x.iteritems(), key=operator.itemgetter(1))[0]
