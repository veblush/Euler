s = open("Q067_triangle.txt").read()

# load grid to 2 dimensional array
g = []
r = []
for w in s.split():
  r.append(int(w))
  if len(r) > len(g):
    g.append(r)
    r = []

# get maximum value by dynamic programming
v = []
for gr in g:
  r = gr[:]
  if len(v) > 0:
    for i in xrange(len(r)):
      r[i] += max(v[-1][i-1] if i > 0 else 0,
                  v[-1][i] if i < len(v[-1]) else 0)
  v.append(r)
print max(v[-1])
