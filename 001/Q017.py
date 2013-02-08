lens = lambda a: [len(s) for s in a]

a = lens(["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
b = lens(["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"])
c = lens(["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"])

x = (sum(a) +
     sum(b) +
     sum(c) * 10 + sum(a) * 8)

y = (x +
     sum(a) * 100 + len("hundred") * 900 + len("and") * 891 + x * 9 +
     len("onethousand"))

print y
