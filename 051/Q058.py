import sys
import math

# ready prime array
primes = [2]
for i in xrange(3, 100000):
  ii = int(math.sqrt(i))
  composite = False
  for p in primes:
    if p > ii:
      break
    if i % p == 0:
      composite = True
      break
  if not composite:
    primes.append(i)

def is_prime(n):
  nn = int(math.sqrt(n))
  for p in primes:
    if p > nn:
      break
    if n % p == 0:
      return False
  return True

pc, cc = 0, 1
s = 1
for i in xrange(1, 100000):
  ks = [s + i*2, s + i*2*2, s + i*2*3, s + i*2*4]
  for k in ks:
    if is_prime(k):
      pc += 1
    else:
      cc += 1
    p = float(pc) / (pc + cc)
    if p < 0.1:
      print i*2+1
      sys.exit()
  s += i*2*4
