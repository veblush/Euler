import math

def run(n):
  nn = int(math.sqrt(n))
  fs = []
  for i in xrange(2, nn):
    if n % i == 0:
      if any(i % f == 0 for f in fs) == False:
        fs.append(i)
        print i

run(13195)
run(600851475143)
