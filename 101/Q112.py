def mono(n):
  s = str(n)
  return (all(ord(s[i]) <= ord(s[i+1]) for i in xrange(len(s)-1)) or
          all(ord(s[i]) >= ord(s[i+1]) for i in xrange(len(s)-1)))

b, c = 0, 0
for i in xrange(1, 1000000000):
  if mono(i):
    c += 1
  else:
    b += 1
  if float(b)/(b+c) >= 0.99:
    print i
    break
