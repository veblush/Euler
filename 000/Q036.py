def is_palindrome(s):
  return s[:len(s)/2] == s[-1:-(len(s)/2)-1:-1]

s = []
for i in xrange(1, 1000000):
  if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
    s.append(i)
print sum(s), s
