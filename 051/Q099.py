import math

data = [s.strip().split(",") for s in open("Q099_base_exp.txt")]
vals = [float(e)*math.log(float(b)) for b, e in data]
print sorted(enumerate(vals, start=1), key=lambda x: x[1])[-1]
