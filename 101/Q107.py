# load network matrix
m = []
for line in open("Q107_network.txt"):
  r = [int(a) if a != "-" else 10000 for a in line.strip().split(",")]
  m.append(r)

# solve with prim's algorithm
s = [[0]*len(m) for _ in range(len(m))]
a = set(range(len(m)))
y = set([0])
while len(y) < len(m):
  r = min(((m[v][w], v, w) for w in (a-y) for v in y), key=lambda x: x[0])
  y.add(r[2])
  s[r[1]][r[2]] = r[0]
  s[r[2]][r[1]] = r[0]

C = sum(m[v][w] if m[v][w] != 10000 else 0 for v in xrange(len(m)) for w in xrange(len(m)))/2
D =sum(s[v][w] for v in xrange(len(s)) for w in xrange(len(s)))/2
print C - D
