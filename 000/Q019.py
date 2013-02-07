def is_leap_year(y):
  return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

def get_month_days(y, m):
  if m in (1, 3, 5, 7, 8, 10, 12):
    return 31
  elif m in (4, 6, 9, 11):
    return 30
  else:
    return 29 if is_leap_year(y) else 28

v = 0
d = 0
for y in xrange(1900, 2000+1):
  for m in xrange(1, 12+1):
    if y >= 1901 and d % 7 == 6:
      v += 1
    d += get_month_days(y, m)

print v
