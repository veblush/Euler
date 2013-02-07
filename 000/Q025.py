a = 1
b = 1
i = 2
while True:
  a, b = b, a + b
  i += 1
  if len(str(b)) == 1000:
    print i
    break 
