def run(f):
  m = []
  for l in open(f):
    m.append([int(v) for v in l.split(",")])
  k = [[1000000]*len(m[0]) for y in xrange(len(m))]
  q = [(0, 0)]
  k[0][0] = m[0][0]
  while len(q) > 0:
    x, y = q.pop()
    if x > 0:
      p = k[y][x] + m[y][x-1]
      if k[y][x-1] > p:
        k[y][x-1] = p
        q.append((x-1, y))
    if x < len(m[0])-1:
      p = k[y][x] + m[y][x+1]
      if k[y][x+1] > p:
        k[y][x+1] = p
        q.append((x+1, y))
    if y > 0:
      p = k[y][x] + m[y-1][x]
      if k[y-1][x] > p:
        k[y-1][x] = p
        q.append((x, y-1))
    if y < len(m)-1:
      p = k[y][x] + m[y+1][x]
      if k[y+1][x] > p:
        k[y+1][x] = p
        q.append((x, y+1))
  print k[-1][-1]

run("Q081_test.txt")
run("Q081_matrix.txt")
