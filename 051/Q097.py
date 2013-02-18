M=10000000000
a=28433
b=7830457

v = 1
x = 2**1000 % M
for i in xrange(b/1000):
  v = (v * x) % M
v = (v * 2**(b % 1000)) % M

print (a*v+1)%M
