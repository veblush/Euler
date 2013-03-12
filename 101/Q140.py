import math

# c = (3x*x + x) / (1 - x - x*x)
# -> (3+c)*x*x +(c+1)*x - c = 0
# -> b^4-4ac = 5*c*c + 14*c +1 -> should be k*k form
# acually it might be solved with pell equation but
# I use a dirty shortcut :)

r, s, c = 0, 0, 1
while True:
  a = 5*c*c + 14*c +1
  aa = int(math.sqrt(a))
  if aa*aa == a:
    r, s = r + 1, s + c
    if r == 30:
      print s
      break
    # jump for fast calculation
    # factor was from experiment
    if r % 2 == 0:
      c = int(c * 3.535322)
    else:
      c = int(c * 1.938748)
  else:
    c += 1
