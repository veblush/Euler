from itertools import *

digits = 10
nth = 1000000
print "".join(str(i) for i in islice(permutations(range(digits)), nth-1, nth).next())
