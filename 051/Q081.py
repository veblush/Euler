import copy

def run(f):
  m = []
  for l in open(f):
    m.append([int(v) for v in l.split(",")])
  c = copy.deepcopy(m)
  for y in xrange(len(m)):
    for x in xrange(len(m[0])):
      ax = c[y-1][x] if y > 0 else 0
      ay = c[y][x-1] if x > 0 else 0
      if ax != 0 and ay != 0:
        c[y][x] += min(ax, ay)
      elif ax != 0:
        c[y][x] += ax
      elif ay != 0:
        c[y][x] += ay
  print c[-1][-1]

run("Q081_test.txt")
run("Q081_matrix.txt")
