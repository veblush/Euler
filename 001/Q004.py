def is_palindrome(n):
  s = str(n)
  return s[:len(s)/2] == s[-1:-(len(s)/2)-1:-1]

v = 0
for a in xrange(100, 1000):
  for b in xrange(100, 1000):
    if is_palindrome(a*b):
      v = max(v, a*b)
print v
