tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat_0 = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat_1 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat_0
print fat_cat_1

# Cool code to make an INFINITE timer clock
# while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,