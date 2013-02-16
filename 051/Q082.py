import copy

def run(f):
  M = 1000000
  m = []
  for l in open(f):
    m.append([int(v) for v in l.split(",")])
  c = copy.deepcopy(m)
  for x in xrange(1, len(m[0])):
    a = [0]*len(m)
    for y in xrange(len(m)):
      ax = c[y][x-1]
      ay = a[y-1] if y > 0 else M
      a[y] = c[y][x] + (min(ax, ay) if ax != M or ay != M else 0)
    b = [0]*len(m)
    for y in xrange(len(m)-1, -1, -1):
      ax = c[y][x-1]
      ay = b[y+1] if y < len(m)-1 else M
      b[y] = c[y][x] + (min(ax, ay) if ax != M or ay != M else 0)
    for y in xrange(len(m)):
      c[y][x] = min(a[y], b[y])
  print min(c[y][-1] for y in xrange(len(m)))

run("Q081_test.txt")
run("Q081_matrix.txt")
