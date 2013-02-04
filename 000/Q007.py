primes = [ 2, ]

n = 3
while True:
  if not any(n % p == 0 for p in primes):
    primes.append(n)
    if len(primes) == 10001:
      break
  n += 1

print primes[-1]
