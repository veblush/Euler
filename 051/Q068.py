import itertools

s = []

for total in xrange(10, 20):
  ns = [x for x in itertools.permutations(xrange(1, 11), 3) if sum(x) == total]
  for i0 in ns:
    for i1 in ns:
      if i0[2] != i1[1]:
        continue
      for i2 in ns:
        if i1[2] != i2[1]:
          continue
        for i3 in ns:
          if i2[2] != i3[1]:
            continue
          for i4 in ns:
            if i3[2] != i4[1] or i4[2] != i0[1]:
              continue
            if len(set(i0 + i1 + i2 + i3 + i4)) != 10:
              continue
            if min(i0[0], i1[0], i2[0], i3[0], i4[0]) != i0[0]:
              continue
            s.append("".join(str(n) for n in i0+i1+i2+i3+i4))

print sorted(s)[-1]
