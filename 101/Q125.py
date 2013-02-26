import math

def is_palindrome(s):
  return s[:len(s)/2] == s[-1:-(len(s)/2)-1:-1]

M = 10**8
m = int(math.sqrt(M)) + 1
t = set()
for i in xrange(1, m + 1):
  x = 0
  for j in xrange(i, m + 1):
    x += j**2
    if x >= M:
      break
    if j > i and is_palindrome(str(x)):
      t.add(x)
print sum(t)
  