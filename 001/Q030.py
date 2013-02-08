def check_5th(n):
  x = sum(int(c)**5 for c in str(n))
  return x == n

ns = [i for i in xrange(2, 1000000) if check_5th(i)]
print sum(ns), ns
