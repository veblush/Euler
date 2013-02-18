import math

data = [x.strip('"') for x in open("Q098_words.txt").read().split(",")]
nums = []

for dc in xrange(1, 15+1):
  words = [w for w in data if len(w) == dc]

  ss = []
  for i in xrange(int(math.ceil(math.sqrt(10**(dc-1)))),
                  int(math.sqrt(10**dc))):
    ss.append(str(i * i))
  sset = set(ss)

  def f(word, n):
    # construct mapping table
    mp, im = {}, {}
    for c, d in zip(word, n):
      if c in mp:
        if mp[c] != d:
          return None
      else:
        mp[c] = d
        if d in im:
          if im[d] != c:
            return None
        else:
          im[d] = c

    # try to convert words with a table
    for nword in words:
      if sorted(word) != sorted(nword) or word == nword:
        continue
      k = ""
      for c in nword:
        if c not in mp:
          break
        k = k + mp[c]
      else:
        if k in sset:
          return (k, nword)
    return None

  for word in words:
    if len(word) != dc:
      continue
    for n in ss:
      r = f(word, n)
      if r:
        #print (n, word), r
        nums.append(int(n))
        nums.append(int(r[0]))

print max(nums)
