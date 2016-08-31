from sys import exit

def gold_room():
	"""Function for when user enters the gold room. Can win or calls dead() fucntion"""
	print "This room is full of gold. How many pieces can you take?"

	next = raw_input("> ").lower()

	# Updated code to work with all integers
	try:
		how_much = int(next)
	except  ValueError:
		 dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	"""Function for when user enters the bear_room"""
	print "These ia bear in here!"
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ").lower()

		if next == "take honey":
			dead("The bear looks at you and slaps your face off.")
		elif next == "taunt bear" and not bear_moved: 
			print "The bear has moved from the door. You can go through now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved: #if you type taunt bear twice you die
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means. Try again:"

def chtulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insance."
	print "Do you flee for you life or eat your hear?"

	next = raw_input("> ").lower()

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		chtulhu_room()

def dead(why):
	print why, "You DIE. Good Job!!!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ").lower()

	if next == "left":
		bear_room()
	elif next == "right":
		chtulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()
