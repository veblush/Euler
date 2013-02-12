import math

# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
def q(x):
  xx = int(math.sqrt(x))
  yield xx
  m, d, a = 0, 1, xx
  while True:
    m_ = d * a - m
    d_ = (x - m_*m_) / d
    a_ = (xx + m_) / d_
    yield a_
    m, d, a = m_, d_, a_

# http://en.wikipedia.org/wiki/Continued_fraction
def f(x):
  rgen = q(x)
  r0 = rgen.next()
  r1 = rgen.next()
  h0, h1 = r0, r1 * r0 + 1
  k0, k1 = 1, r1
  if h1*h1 - x*k1*k1 == 1:
    return (h1, k1)

  while True:
    r = rgen.next()
    h = r * h1 + h0
    k = r * k1 + k0
    if h*h - x*k*k == 1:
      return (h, k)
    h0, h1 = h1, h
    k0, k1 = k1, k
  return None

s = []
for d in xrange(2, 1001):
  dd = int(math.sqrt(d))
  if dd*dd == d:
    continue
  s.append((d, f(d)))
print sorted(s, key=lambda x: -x[1][0])[0][0]
