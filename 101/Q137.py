# s(x) = x / (1-x-x*x)
#    c = x / (1-x-x*x)
# ->
# (c+1)**2 + (2c)**2 == k**2  (c, k is integer)
# enumerate fibonacci triangle and check a constraint

r = 1
a, b, c = 3, 4, 5
x, y = 3, 5
while True:
  x, y = y, x+y
  x, y = y, x+y
  a, b, c = x-a, a+b+c, y
  #print x, y, a, b, c
  if (a-1)*2 == b:
    r += 1
    if r == 15:
      print a-1
      break
