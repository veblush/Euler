import sys
import itertools

def digit4s(f):
  r = []
  n = 1
  while True:
    v = f(n)
    if v >= 10000:
      return r
    if v >= 1000:
      r.append(str(v))
    n += 1

t = [
  digit4s(lambda n: n*(n+1)/2),
  digit4s(lambda n: n*n),
  digit4s(lambda n: n*(3*n-1)/2),
  digit4s(lambda n: n*(2*n-1)),
  digit4s(lambda n: n*(5*n-3)/2),
  digit4s(lambda n: n*(3*n-2))]

for t0, t1, t2, t3, t4, t5 in itertools.permutations(range(0, 6), 6):
  for a in t[t0]:
    for b in t[t1]:
      if a[2:] != b[:2]:
        continue
      for c in t[t2]:
        if b[2:] != c[:2]:
          continue
        for d in t[t3]:
          if c[2:] != d[:2]:
            continue
          for e in t[t4]:
            if d[2:] != e[:2]:
              continue
            for f in t[t5]:
              if e[2:] != f[:2] or a[:2] != f[2:]:
                continue
              print int(a)+int(b)+int(c)+int(d)+int(e)+int(f), [a, b, c, d, e, f]
              sys.exit()
