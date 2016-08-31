class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		print "\n"
		print "-" * 10
		for line in self.lyrics:
			print line

	def song_length(self, content):
		song_length = len(self.lyrics)
		print content, song_length

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right here"])

bulls_song = ["They rally around the family", "With pockets full of shells"]

bulls_on_parade = Song(bulls_song)

happy_bday.sing_me_a_song()
happy_bday.song_length("What that long:")

bulls_on_parade.sing_me_a_song()
bulls_on_parade.song_length("Really two argments?")