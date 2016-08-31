numbers = []

def count(list,increment):
	i = 0
	while i < 6:
		print "At the top i is %d" % i
		list.append(i)

		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

count(numbers,5)

print "The numbers: "

for num in numbers:
	print num 