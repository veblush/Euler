#def run(s, n):
#  print s
#  if s > n:
#    return 0
#  if (s-1) % 3 == 0 and ((s-1)/3) % 2 != 0 and s > 4:
#    return 1 + max(run((s-1) / 3, n), run(s*2, n))
#  else:
#    return 1 + run(s*2, n)

def run(n):
  c = [0]*(n)
  c[1] = 1
  for i in xrange(2, n):
    x = i
    l = []
    while True:
      if x < n and c[x] != 0:
        break
      l.insert(0, x)
      x = x / 2 if x % 2 == 0 else x * 3 + 1

    k = c[x]
    for j in l:
      k += 1
      if j < n:
        c[j] = k
  return c.index(max(c))

print run(20)
print run(1000000)
