import math

def f(n):
  seq = []
  a = 1
  b = int(math.sqrt(n))
  seq.append((b, a, b))
  while True:
    a_ = (n - b*b) / a
    s = 1
    while True:
      x = a_ * s
      b_ = x - b
      if 0 <= math.sqrt(n) - b_ < a_:
        break
      s += 1
    for i, p in enumerate(seq):
      if p[1] == a_ and p[2] == b_:
        seq.append((s, a_, b_))
        return seq[i+1:]
    seq.append((s, a_, b_))
    a, b = a_, b_

c = 0
for i in xrange(2, 10000):
  if i == int(math.sqrt(i))**2:
    continue
  if len(f(i)) % 2 != 0:
    c += 1
print c
