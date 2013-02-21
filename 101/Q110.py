import math
import bisect

# ready prime array
primes = [2]
for i in xrange(3, 1000+1):
  ii = int(math.sqrt(i))
  composite = False
  for p in primes:
    if p > ii:
      break
    if i % p == 0:
      composite = True
      break
  if not composite:
    primes.append(i)

f = lambda a: reduce(lambda x, y: x*y, (k+1 for p, k in a))

M = 4000000
m = (M-1)*2
q = [ (4, [(2, 2)]) ]
qs = set([4])
while True:
  x, a = q.pop(0)
  qs.remove(x)
  if f(a) > m:
    print x, f(a), a
    print reduce(lambda x, y: x*y, (p**(k/2) for p, k in a))
    break
  w = []
  for i in range(len(a)+1):
    t = x * primes[i] * primes[i]
    if i < len(a):
      e = a[:i] + [(a[i][0], a[i][1]+2)] + a[i+1:]
    else:
      e = a + [(primes[i], 2)]
    w.append((t, e))
  w = sorted(w, key=lambda x: x[0])
  for k in w:
    if k[0] not in qs:
      bisect.insort_right(q, k)
      qs.add(k[0])
