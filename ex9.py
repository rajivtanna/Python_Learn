# Here's some strange new stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print "Here are the days: ", days
print "Here are the months: ", months

a = """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines is we want, or 5, or 6.
"""


# The belows shows the difference between %s and %r. 
#%r is useful to show how things are actually stores

print "%s" % a
print
print "%r" % a