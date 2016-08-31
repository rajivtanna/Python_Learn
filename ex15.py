from sys import argv

script, filename = argv

text1 = open(filename) #imports the data from the file into the variable text
text2 = open(filename) #imports the data from the file into the variable text
text_read = text1.read()
text_list = text2.readlines()

print "Here's your file %r" % filename
print text_read # Prints the contents of the file to screen
print text_list # Creates a list of strings for each line
print text1.tell()

# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again) #Shows how this can be done using a raw_input

# print txt_again.read()