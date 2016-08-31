from sys import argv
from os.path import exists

script, from_file, to_file = argv

if exists(to_file) == False:
	print "New file created."

open(to_file,'w').write(open(from_file).read())
