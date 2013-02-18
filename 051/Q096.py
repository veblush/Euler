import itertools

def possible(p, x, y):
  a = [False]*10
  for i in xrange(9):
    if p[y][i] != 0 and i != x:
      a[p[y][i]] = True
    if p[i][x] != 0 and i != y:
      a[p[i][x]] = True
  sx, sy = x/3, y/3
  for i, j in itertools.product(xrange(3), xrange(3)):
    xx, yy = sx*3 + i, sy*3 + j
    if p[yy][xx] != 0 and (xx != x or yy != y):
      a[p[yy][xx]] = True
  return [i for i, f in enumerate(a) if i > 0 and not f]

# solve by searching solutions with recursion
def solve(p):
  ls = [(x, y) for x, y in itertools.product(xrange(9), xrange(9)) if p[y][x] == 0]
  def trial(p, ls):
    if len(ls) == 0:
      return p
    tx, ty = ls[0][0], ls[0][1]
    for n in possible(p, tx, ty):
      p[ty][tx] = n
      if trial(p, ls[1:]):
        return p
    p[ty][tx] = 0
    return None
  trial(p, ls)

# read data
ps = []
f = open("Q096_sudoku.txt")
while True:
  if f.readline().strip() != "":
    p = []
    for y in xrange(9):
      l = f.readline()
      r = []
      for x in xrange(9):
        r.append(int(l[x]))
      p.append(r)
    ps.append(p)
  else:
    break

# solve all puzzles
s = 0
for p in ps:
  solve(p)
  s += p[0][0]*100+p[0][1]*10+p[0][2]
print s
