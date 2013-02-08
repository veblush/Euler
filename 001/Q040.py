s = "".join(str(i) for i in xrange(0, 1000000))
v = (s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000])
print v
r = 1
for i in v:
  r *= int(i)
print r
