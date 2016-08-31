name = 'Zed A. Shaw'
age = 35 #not a lie
height_inch = 74 # inches
height_cm = height_inch * 2.54
weight_lbs = 180 #lbs
weight_kg = weight_lbs * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print "Let's talk about %s." % name
print "He's %d inches tall." % height_inch
print "In metrics this is  %d cm tall." % height_cm
print "He's %d pound heavy." % weight_lbs
print "In metrics this is  %d kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_inch, weight_lbs, age + height_inch + weight_lbs)
