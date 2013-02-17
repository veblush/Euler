#
def pytha(p, q):
  a = p[0]*p[0] + p[1]*p[1]
  b = q[0]*q[0] + q[1]*q[1]
  c = (p[0]-q[0])*(p[0]-q[0]) + (p[1]-q[1])*(p[1]-q[1])
  return a+b == c or b+c == a or a+c == b

M = 50
K = M+1
N = K*K
c = 0
for p in xrange(1, N):
  for q in xrange(p+1, N):
    if pytha((p / K, p % K), (q / K, q % K)):
      c += 1
print c
