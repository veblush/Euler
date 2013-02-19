f1, f2 = 1, 1
for i in xrange(3, 10000000):
  f = f1 + f2
  f1, f2 = f2, f
  s = str(f)
  s1, s2 = s[:9], s[-9:]
  if (s1.find("0") == -1 and len(set(s1)) == 9 and
      s2.find("0") == -1 and len(set(s2)) == 9):
    print i, s1, s2
    break
