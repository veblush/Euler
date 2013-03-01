def f(n):
  if n % 2 == 0 or n % 5 == 0:
    return None
  a, d = 1, 1
  while True:
    a = a % n
    if a == 0:
      return d
    a = a * 10 + 1
    d += 1

for n in xrange(1000000, 1100000):
  v = f(n)
  if v > 1000000:
    print n
    break
