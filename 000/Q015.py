import math

# calculate with a simple permutation
def run(n):
  return math.factorial(n*2) / (math.factorial(n)**2)

print run(2)
print run(20)
