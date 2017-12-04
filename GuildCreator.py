import random

#just a random size for the guild; I picked 100
guild_size = 100

class Member(object):

    #Constructor
    def __init__(self, name, strength, defense, speed):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.speed = speed

    #string representation
    def __str__(self):
        to_string = "Name: %s \t Strength: %.1f \t Defense: %.1f \t Speed: %.1f" % (self.name, self.strength, self.defense, self.speed) 
        return to_string

"""Function that actually generates the random members.
Each stat value is a number between 1 - 10 right now but 
we can tweak that. It returns a dictionary of each member."""
def generate():
    members = {}
    for i in range(1, guild_size + 1):
        player_name = "P" + str(i)
        player_strength = (random.random() + .01) * 10
        player_defense = (random.random() + .01) * 10
        player_speed = (random.random() + .01) * 10

        members[player_name] = Member(player_name, player_strength, player_defense, player_speed)
    return members

"""Defining main didn't actually work so I just wrote the 
code on its own outside of any function"""
#def main():  
guild = generate()
for member in guild:
    print(str(guild[member]))