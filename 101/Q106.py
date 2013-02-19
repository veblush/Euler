import itertools

n = 12
c = 0
for i in range(2, n/2+1):
  for a in itertools.combinations(xrange(n), i):
    except_a = sorted(list(set(range(n)) - set(a)))
    for b in itertools.combinations(except_a, i):
      if min(a) > min(b):
        continue
      if any(i > j for i, j in zip(a, b)):
        c += 1
print c
