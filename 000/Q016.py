def run(n):
  x = str(2**n)
  return sum(int(c) for c in x)

print run(15)
print run(1000)
