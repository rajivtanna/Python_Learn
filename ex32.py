the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pears', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is the count %d" % number

# same as the above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also can go through mixed type lists but need to use %r as don't know what the type is
for i in change:
	print "I got %r" % i

elements = []
elements1 = range(11,16)

# we can use the range function to append items to the list
for i in range(1, 6):
	print "Adding %d to the list." % i
	elements.append(i)

# now we can print them

for i in elements:
	print "Element was: %d" % i

print "Test:", elements
print "Test1:", elements1