def is_palindrome(s):
  return s[:len(s)/2] == s[-1:-(len(s)/2)-1:-1]

c = 0
for i in xrange(1, 10000):
  v = i
  for x in xrange(50):
    v += int(str(v)[::-1])
    if is_palindrome(str(v)):
      break
  else:
    c += 1
print c
