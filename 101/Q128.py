import math

# ready prime array
primes = [2]
for i in xrange(3, 1000000+1):
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
pset = set(primes)

def g(layer):
  # generate (layer, start, end)
  def f(layer):
    yield (0, 1, 1)
    yield (1, 2, 7)
    s = 2
    d = 0
    for l in xrange(layer):
      d += 1
      s += d * 6
      yield (l+2, s, s + ((d+1) * 6) - 1)

  # scan from layer 2
  layers = f(layer)
  l = (None, layers.next(), layers.next())
  for l_next in layers:
    l = l[1:] + (l_next,)
    d_0 = l[1][1] - l[0][1]
    d_1 = l[2][1] - l[1][1]
    i = 0
    yield (i + l[1][1], 
            (1, l[1][2] - l[1][1],
             l[2][2] - (i + l[1][1]), d_1, d_1+1, 
             d_0))
    if l[1][0] > 1:
      i += 6 * (l[1][0]-1) + 5
      d_0 += 5
      d_1 += 5
      yield (i + l[1][1],
              (1, l[1][2] - l[1][1],
               d_1, d_1+1, 
               d_0+1, d_0 + (l[0][2] - l[0][1] + 1)))

x = 1
for k in g(10000000):
  c = 0
  for d in k[1]:
    if d in pset:
      c += 1
  if c == 3:
    x += 1
    if x == 2000:
      print k[0]
      break
