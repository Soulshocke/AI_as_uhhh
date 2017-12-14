#GuildCreator.py 2.0.0
import random
import QuestCreator

#just a random size for the guild; I picked 100
guild_size = 100

#I chose random orc names to input for the names list. I simply generated a list online and manually and input them.
names = ["Maton", "Hardurosh", "Lamthak", "Kelum", "Sorgargor", "Zavtarram", \
 "Dradran", "Borus", "Kruban", "Mokdurgron", "Hurdurguld", "Ukogus", "Samfur"]

"""Member class notes: 
The class comes with a constructor which includes a 
player name, level, attack, defense, and speed. The 
class also comes with a str function to represent Member
objects as strings"""
class Member(object):

    #Constructor
    def __init__(self, name, level, _type, attack, defense, speed):
        self.name = name
        self.level = level
        self._type = _type
        self.attack = attack
        self.defense = defense
        self.speed = speed

    #string representation
    def __str__(self):
        to_string = "Name: %s\t Level: %02.0d\t Type: %s \t ATK: %02.0f\t DEF: %02.0f\t SPD: %02.0f" %\
                    (self.name.ljust(15), self.level, self._type.ljust(8), self.attack, self.defense, self.speed) 
        return to_string

"""set_skills() notes:
Using random numbers, we are going to randomly
select whether a player will be an attacker, defender,
or runner then from there the stat that corresponds with 
the specialty will take up between 60 - 80% of the stat points.
Attacker --> attack
Defender --> Defense 
Runner --> Speed
The secondary stat can either be picked randomly or not. For now
I have decided to pick it myself:
Attacker: More inclined to have better speed stat for faster strikes as opposed to more defense
Defender: More inclined to have better attack in case enemy gets too close. Logically it makes sence 
because defenders wear heavy armor anyways so speed makes no sense
Runners: Prefer attack since they are really squishy, thee is a better chance of survival 
if they hit and desorient an enemy.
"""
def set_skills(level):
    player_type = None
    skill_points = level * 2
    stats = []
    random_num = random.random()

    attack = 0
    defense = 0
    speed = 0

    #randomly generated number will determine what 
    #the player will specialize in
    # *** [Debug note] Switched randrange with randint ***
    if random_num <= .33:
        player_type = "Attacker"
        attack_percentage = random.randint(60, 80) / 100
        attack = int(skill_points * attack_percentage)

        speed = random.randint(1, skill_points - attack)
        defense = skill_points - attack - speed

    elif random_num > .33 and random_num <= .66:
        player_type = "Defender"
        defense_percentage = random.randint(60, 80) / 100
        defense = int(skill_points * defense_percentage)

        attack = random.randint(1, skill_points - defense)
        speed = skill_points - attack - defense

    else:
        player_type = "Runner"
        speed_percentage = random.randint(60, 80) / 100
        speed = int(skill_points * speed_percentage)

        attack = random.randint(1, skill_points - speed)
        defense = skill_points - attack - speed
    
    stats.append(player_type)
    stats.append(attack)
    stats.append(defense)
    stats.append(speed)

    return stats 

def name_generator(names):
	random_num = random.randint(1, 10)
	new_name = ""

	if random_num == 1:
		return random.choice(names)

	elif random_num >= 2 and random_num <= 9:
		first_name = random.choice(names)
		second_name = random.choice(names)
		while new_name in names or new_name == "":
			random_num = random.randint(1,10)

			if random_num <= 5:
				random_num = random.randint(1,10)

				if random_num <= 5:
					new_name = first_name[ :int(len(first_name)/2)] + second_name[int(len(second_name)/2): ]
				else:
					new_name = first_name[int(len(first_name)/2): ] + second_name[ :int(len(second_name)/2)]
			else:
				random_num = random.randint(1,10)

				if random_num <= 5:
					new_name = second_name[ :int(len(second_name)/2)] + first_name[int(len(first_name)/2): ]
				else:
					new_name = second_name[int(len(second_name)/2): ] + first_name[ :int(len(first_name)/2)]
	else:
		new_name = random.choice(names)
		new_name = new_name[::-1]
		while(new_name in names):
			new_name = random.choice(names)
			new_name = new_name[::-1]

	new_name = new_name.lower().capitalize()
	if new_name not in names:
		names.append(new_name)
	return new_name

#Generate just creates the entire guild using set_skills()
# *** [Debug note] Switched randrange with randint ***
def generate():
    members = {}
    for i in range(1, guild_size + 1):
        player_ID = "P" + str(i)
        player_name = name_generator(names)
        player_level = random.randint(5,50) #50 is max level for this
        player_type, attack, defense, speed = set_skills(player_level)
        # print("i = {0}: " .format(i))
        # print("         {0}, {1}, {2}, {3}" \
        #     .format(player_type, attack, defense, speed))

        members[player_ID] = Member(player_name, player_level, player_type, attack, defense, speed)
    return members

# To test this file
# if __name__ == "__main__":

    # questBoard = {}
    # guild = generate()

    #Print all generated Guild members
    # for member in guild:
    #     print(str(guild[member]))

    #Prompt user to create a quest object, add it to questBoard
    # title, _type, diff, size = QuestCreator.create_quest()
    # questBoard[title] = QuestCreator.Quest(title, _type, diff, size)

    #Print all quests on questBoard
    # for post in questBoard:
    #     print(questBoard[post])
