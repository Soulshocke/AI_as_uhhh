#QuestCreator.py
#Contians quest object and funciton create_quest that will prompt user to
#create a quest with a defining title, type, difficulty, and max Party Size

#Quest object
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

#Create quest series of prompts
def create_quest():
	title = ""
	_type = ""
	diff = 0
	size = 0
	quest = []

	#Set Type
	print("What type of quest would you like to create? (Bounty, Escort, Fetch)")
	_type = input()
	while (True): 		#Ensures specific type is picked
		if _type.lower() == "bounty":
			_type = "bounty"
			break
		elif _type.lower() == "escort":
			_type = "escort"
			break
		elif _type.lower() == "fetch":
			_type = "fetch"
			break
		print("Invalid type. Type again (Bounty, Escort, Fetch)")
		_type = input()

	#Set Difficulty
	print("Select a difficulty, easy(1) to difficult(100)")
	diff_in = input()
	diff = int(diff_in)
	while(diff > 100 or diff < 1):		#Ensures legal difficulty level
		print("Please pick a number between 1 - 100")
		diff_in = input()
		diff = int(diff_in)

	#Set Max Input Size
	print("What will be the Max party size for this quest? (Limit to how many people can go on the quest)")
	size_in = input()
	size = int(size_in)
	while(size < 1):		#Ensures legal party size
		print("Please pick a value greater than 0")
		size_in = input()
		size = int(size_in)

	#Set Title
	print("What would you like to name your quest?")
	title = input()
	while(True):			#Ensures User types a correct name
		print("%s, is that right? y/n" % (title))
		final = input()
		if final.lower() == "y":
			break
		elif final.lower() == "n":
			print("What would you liek to name your quest?")
			final = input()
		else:
			print("Invalid input. Type y or n.")

	#Append features to quest array
	quest.append(title)
	quest.append(_type)
	quest.append(diff)
	quest.append(size)

	return quest

#If you just want to test the Quest funcitonality,
#uncomment the block below and run:
#python QuestCreator.py

'''
questBoard = {}
title, _type, diff, size = create_quest()
questBoard[title] = Quest(title, _type, diff, size)
for post in questBoard:
	print(questBoard[post])
'''