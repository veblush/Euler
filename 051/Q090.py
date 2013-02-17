import itertools

sn = [(a*a/10, a*a%10) for a in range(1, 10)]

def check(cs):
  for s in sn:
    c = (s[0] if s[0] != 9 else 6, s[1] if s[1] != 9 else 6)
    if c[0] in cs[0] and c[1] in cs[1]:
      continue
    if c[0] in cs[1] and c[1] in cs[0]:
      continue
    return False
  return True

ck = [set(x) for x in itertools.combinations(xrange(0, 10), 6)]
for s in ck:
  if 9 in s:
    s.remove(9)
    s.add(6)

c = 0
for x in xrange(len(ck)):
  for y in xrange(x, len(ck)):
    if check((ck[x], ck[y])):
      c += 1
print c
