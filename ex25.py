def break_words(stuff):
	"""This function will break words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	word = words.pop(-1)
	print word

def sort_sentance(sentance):
	"""Takes in a full sentance and returns sorted words."""
	words = break_words(sentance)
	return sort_words(words)

def print_first_and_last(sentance):
	"""Print the first and the last words of the sentance."""
	words = break_words(sentance)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentance):
	"""Print the first and the last words of the sentance."""
	words = sort_sentance(sentance)
	print_first_word(words)
	print_last_word(words)
