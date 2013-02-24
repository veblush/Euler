import bisect

t = 0
a = [(1, 1, i) for i in range(2, 20)] # value, num, power
while True:
  c = a.pop(0)
  if c[0] >= 10 and sum(int(x) for x in str(c[0])) == c[1]:
    t += 1
    if t == 30:
      break
  c = ((c[1]+1)**(c[2]), c[1]+1, c[2])
  bisect.insort_left(a, c)

print c[0]
