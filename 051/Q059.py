import itertools

e = [int(v) for v in open("Q059_cipher1.txt").read().strip().split(",")]

for k in itertools.permutations(xrange(ord("a"), ord("z")+1), 3):
  d = [k[i % 3] ^ c for i, c in enumerate(e)]
  p = "".join(chr(c) for c in d)
  if (p.find("is") != -1 and p.find("the") != -1 and
      p.find("are") != -1 and p.find("was") != -1):
    print sum(ord(c) for c in p), p[:200]
