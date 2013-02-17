def p(n):
  return sum([int(c)**2 for c in str(n)])

lm = {}
def f(n):
  if n == 1 or n == 89:
    return n
  if n in lm:
    return lm[n]
  y = p(n)
  if y != 1 and y != 89:
    y = f(y)
  lm[n] = y
  return y

c = 0
for i in xrange(1, 10000000):
  if f(p(i)) == 89:
    c += 1
print c