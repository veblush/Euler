ru = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}

def roman_to_int(s):
  v = 0
  for i, c in enumerate(s):
    d = ru[c]
    if i < len(s)-1 and d < ru[s[i+1]]:
      v -= d
    else:
      v += d
  return v

def int_to_roman(i):
  n = i
  s = ""
  if n >= 1000:
    d = n / 1000
    if d >= 1: s += "M" * d
    n -= d * 1000
  if n >= 100:
    d = n / 100
    if   d == 9: s += "CM"
    elif d >= 5: s += "D" + "C" * (d-5)
    elif d == 4: s += "CD"
    elif d >= 1: s += "C" * d
    n -= d * 100
  if n >= 10:
    d = n / 10
    if   d == 9: s += "XC"
    elif d >= 5: s += "L" + "X" * (d-5)
    elif d == 4: s += "XL"
    elif d >= 1: s += "X" * d
    n -= d * 10
  if n >= 1:
    d = n
    if   d == 9: s += "IX"
    elif d >= 5: s += "V" + "I" * (d-5)
    elif d == 4: s += "IV"
    elif d >= 1: s += "I" * d
    d -= n
  return s

r = 0
for line in open("Q089_roman.txt"):
  s = line.strip()
  x = roman_to_int(s)
  n = int_to_roman(x)
  r += len(s) - len(n)
print r
