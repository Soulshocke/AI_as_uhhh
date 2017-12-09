#GuildCreator.py 2.0.0
import random
import QuestCreator

#just a random size for the guild; I picked 100
guild_size = 100

"""Member class notes: 
The class comes with a constructor which includes a 
player name, level, attack, defense, and speed. The 
class also comes with a str function to represent Member
objects as strings"""
class Member(object):

    #Constructor
    def __init__(self, name, level, attack, defense, speed):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.speed = speed

    #string representation
    def __str__(self):
        to_string = "Name: %s \t Level: %02.0d \t attack: %02.0f \t Defense: %02.0f \t Speed: %02.0f" % (self.name, self.level, self.attack, self.defense, self.speed) 
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
    if random_num <= .33:
        player_type = "Attacker"
        attack_percentage = random.randrange(60, 81) / 100
        attack = int(skill_points * attack_percentage)

        speed = random.randrange(0, skill_points - attack)
        defense = skill_points - attack - defense + 1

    elif random_num > .33 and random_num <= .66:
        player_type = "Defender"
        defense_percentage = random.randrange(60, 81) / 100
        defense = int(skill_points * defense_percentage)

        attack = random.randrange(0, skill_points - defense)
        speed = skill_points - attack - defense + 1

    else:
        player_type = "Runner"
        speed_percentage = random.randrange(60, 81) / 100
        speed = int(skill_points * speed_percentage)

        attack = random.randrange(0, skill_points - speed)
        defense = skill_points - attack - defense + 1
    
    stats.append(attack)
    stats.append(defense)
    stats.append(speed) 

    return stats 

#Generate just creates the entire guild using set_skills()
def generate():
    members = {}
    for i in range(1, guild_size + 1):
        player_name = "P" + str(i)
        player_level = random.randrange(1,51) #50 is max level for this
        attack, defense, speed = set_skills(player_level)

        members[player_name] = Member(player_name, player_level, attack, defense, speed)
    return members


# To test this file
if __name__ == "__main__":

    # questBoard = {}
    # guild = generate()

    # #Print all generated Guild members
    # for member in guild:
    #     print(str(guild[member]))

    # #Prompt user to create a quest object, add it to questBoard
    # title, _type, diff, size = QuestCreator.create_quest()
    # questBoard[title] = QuestCreator.Quest(title, _type, diff, size)

    # #Print all quests on questBoard
    # for post in questBoard:
    #     print(questBoard[post])