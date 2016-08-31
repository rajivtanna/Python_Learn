# argv stands for "Argument Variable". 
# It holds the arguments you pass to your Python script when you run it
from sys import argv

# This unpacks the argv varibale into four variables in this scripts
script, surname, country, city = argv

user_name = raw_input("What is your first name? ")

print "The script is called: ", script
print "You live in: ", city
print "Which is in: ", country 
print "Thanks for that information,", user_name, surname