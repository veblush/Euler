import math

# x = (1 + sqrt(1 + 2n*(n-1))) / 2
# we can get n by pell's equation: (k)**2 - 2(h**2) = -1, k=2n-1

# continued fraction
def cf_2():
  a = 2
  h_2, k_2 = 1, 1
  h_1, k_1 = a*h_2 + 1, a
  yield (h_2, k_2)
  yield (h_1, k_1)
  while True:
    h = a*h_1 + h_2
    k = a*k_1 + k_2
    h_2, k_2 = h_1, k_1
    h_1, k_1 = h, k
    yield (h, k)

# find possible solutions by enumerating continued fraction
for a, b in cf_2():
  if a*a - 2*b*b == -1:
    if a % 2 == 1:
      n = (a+1)/2
      if n > 1000000000000:
        ba = (1 + int(math.sqrt(1 + 2*n*(n-1))))
        if ba % 2 == 0:
          print ba / 2
          break

