class Quest(object):

	#Constructor
	def __init__(self, title, _type, diff, size):
		self.title = title
		self._type = _type
		self.diff = diff
		self.size = size

	#String Rep
	def __str__(self):
		to_string = "Quest: %s \tType: %s \tDifficulty: %d /100 \tMax Party Size: %d" % (self.title, self._type, self.diff, self.size)
		return to_string

def create_quest():
	title = ""
	_type = ""
	diff = 0
	size = 0
	quest = []


	_type = raw_input("What type of quest would you like to create? (Bounty, Escort, Fetch)")
	while (True):
		if _type.lower() == "bounty":
			_type = "bounty"
			break
		elif _type.lower() == "escort":
			_type = "escort"
			break
		elif _type.lower() == "fetch":
			_type = "fetch"
			break
		_type = raw_input("Invalid type")

	diff_in = raw_input("Select a difficulty, easy(1) to difficult(100)")
	diff = int(diff_in)
	while(diff > 100 || diff < 1):
		diff_in = raw_input("Please pick a number between 1 - 100")
		diff = int(diff_in)

	size_in = raw_input("What will be the Max party size for this quest? (Limit to how many people can go on the quest)")
	size = int(size_in)
	while(size > 0):
		size_in = raw_input("Please pick a value greater than 0")
		size = int(size_in)

	title = raw_input("What would you like to name your quest?")
	while(True):
		final = raw_input("%s, is that right? y/n" % (title))
		if final.lower() == "y":
			break
		elif final.lower() == "n":
			final = raw_input("What would you liek to name your quest?")
		else:
			print("Invalid input")

	quest.append(title, _type, diff, size)

	return quest

	
