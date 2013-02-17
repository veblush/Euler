import random

bo = """
  GO A1 CC A2 T1 R1 B1 CH B2 B3 JAIL
  C1 U1 C2 C3 R2 D1 CC D2 D3 FP
  E1 CH E2 E3 R3 F1 F2 U2 F3 G2J
  G1 G2 CC G3 R4 CH H1 T2 H2""".split()

roll = lambda: random.randint(1, 4)

bc = [0] * len(bo)
c = 0
for cc in xrange(100000):
  bc[c] += 1
  d1, d2 = roll(), roll()
  c = (c + d1 + d2) % len(bo)
  if bo[c] == "G2J":
    c = 10
  elif bo[c] == "CC":
    t = random.randint(1, 16)
    if t == 1:    # Advance to GO
      c = 0
    elif t == 2:  # Go to JAIL
      c = 10
  elif bo[c] == "CH":
    t = random.randint(1, 16)
    if t == 1:    # Advance to GO
      c = 0
    elif t == 2:  # Go to JAIL
      c = 10
    elif t == 3:  # Go to C1
      c = 11
    elif t == 4:  # Go to E3
      c = 24
    elif t == 5:  # Go to H2
      c = 39
    elif t == 6:  # Go to R1
      c = 5
    elif t == 7:  # Go to next R (railway company)
      while True:
        c = (c + 1) % len(bo)
        if bo[c][0] == "R":
          break
    elif t == 8:  # Go to next R
      while True:
        c = (c + 1) % len(bo)
        if bo[c][0] == "R":
          break
    elif t == 9:  # Go to next U (utility company)
      while True:
        c = (c + 1) % len(bo)
        if bo[c][0] == "U":
          break
    elif t == 10: # Go back 3 squares.
      c -= 3

bc_sum = sum(bc)
tags = sorted([(i, bo[i], v * 10000 / bc_sum / 100.0) for i, v in enumerate(bc)],
              key=lambda x: -x[2])
print tags[:3]
