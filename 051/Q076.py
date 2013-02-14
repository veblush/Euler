# Intermediate function
# http://en.wikipedia.org/wiki/Partition_(number_theory)

n = 100
a = [[0] * (n+1) for x in xrange(n+1)]
for i in xrange(1, n+1):
  a[i][i] = 1
  for k in xrange(i-1, 0, -1):
    a[i][k] = a[i][k+1] + a[i-k][k]

print a[n][1] - 1
