def sub(a, b):
  i = 0
  for c in a:
    if c == b[i]:
      i += 1
      if len(b) == i:
        return 0
  return len(b) - i

ks = open("Q079_keylog.txt").read().split()
i = 100
while True:
  p = str(i)
  for k in ks:
    d = sub(p, k)
    if d > 0:
      break
  else:
    print p
    break
  i += 10**(d-1)
