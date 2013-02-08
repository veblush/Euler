import math

def gen_pythagorean_triplet(n):
  for a in xrange(1, n/3):
    for b in xrange(a+1, n/2):
      p = a*a + b*b
      c = int(math.sqrt(p))
      if p == c ** 2:
        yield (a, b, c)

for a, b, c in gen_pythagorean_triplet(1000):
  if a + b + c == 1000:
    print a, b, c, a*b*c
