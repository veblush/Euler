tris = set(i*(i+1)/2 for i in xrange(1, 10000))
words = sorted(s.strip('"') for s in open("Q042_words.txt").read().split(","))
r = 0
for word in words:
  v = sum(ord(c) - ord('A') + 1 for c in word)
  if v in tris:
    r += 1
print r
