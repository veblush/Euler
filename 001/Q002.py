def run(n):
  a = 1
  b = 2
  s = 2
  while True:
    a, b = b, a+b
    if b > n:
      break
    if b % 2 == 0:
      s += b
  return s

print run(10)
print run(4000000)

