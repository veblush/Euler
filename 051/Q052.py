f = lambda x: sorted(str(x))

i = 1
while True:
  s = f(i)
  if (s == f(i*2) and
      s == f(i*3) and
      s == f(i*4) and
      s == f(i*5) and
      s == f(i*6)):
    print i
    break
  i += 1