names = sorted(s.strip('"') for s in open("Q022_names.txt").read().split(","))
v = 0
for i, names in enumerate(names):
  name_v = sum(ord(c) - ord('A') + 1 for c in names)
  v += name_v * (i+1)
print v
