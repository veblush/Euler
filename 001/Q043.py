import itertools

s = []
for v in itertools.permutations(range(10)):
  if ((v[1]*100+v[2]*10+v[3]) % 2 == 0 and
      (v[2]*100+v[3]*10+v[4]) % 3 == 0 and
      (v[3]*100+v[4]*10+v[5]) % 5 == 0 and
      (v[4]*100+v[5]*10+v[6]) % 7 == 0 and
      (v[5]*100+v[6]*10+v[7]) % 11 == 0 and
      (v[6]*100+v[7]*10+v[8]) % 13 == 0 and
      (v[7]*100+v[8]*10+v[9]) % 17 == 0):
    s.append(sum(10**(9-i)*k for i, k in enumerate(v)))
print sum(s), s
