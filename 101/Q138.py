import itertools

# generalized continued fraction
def cf(b0, a, b):
  A1, B1 = b0, 1
  yield (A1, B1)
  ai, bi = a.next(), b.next()
  A2, B2 = bi*A1 + ai, bi
  yield (A2, B2)
  while True:
    A0, A1, B0, B1 = A1, A2, B1, B2
    ai, bi = a.next(), b.next()
    A2, B2 = bi*A1 + ai*A0, bi*B1 + ai*B0
    yield (A2, B2)

# solve pell's equation (m-2*n)**2 - 5*n = +-1
# m*m-n*n, 2*m*n
r, c = 0, 0
for h, k in cf(2, itertools.cycle([1]), itertools.cycle([4])):
  if abs(h*h-5*k*k) == 1:
    m, n = h+2*k, k
    L = m*m+n*n
    r, c = r + L, c + 1
    if c == 12:
      print r
      break
