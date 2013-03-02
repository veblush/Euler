import math

# ready prime array
primes = [2]
for i in xrange(3, 1100000):
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

def f(p, q):
  b = 10**(int(math.log10(p)) + 1)
  c = p
  s = b % q
  k = 0
  while True:
    d = max(1, (q - c) / s)
    c = (c + d * s) % q
    #c = (c + s) % q
    k += d
    if c == 0:
      return b * k + p
    
  return 0

s = 0
for i in xrange(len(primes)-1):
  p = primes[i]
  q = primes[i+1]
  if p < 5 or p > 1000000:
    continue
  k = f(p, q)
  s += k
print s
