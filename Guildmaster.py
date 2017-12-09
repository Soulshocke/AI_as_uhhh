# Guildmaster.py

from random import randint, random, choice

'''
    AI as Guildmaster runs on a genetic algorithm where the individual is
    an instance of party composition, and the genome is a combination of 
    party members with their stats.
'''

# *** Defines individual as a dictionary-type party of guild members, 
#     constrained by quest requirements.
#
# Arguments: (dict) guild, (Object) quest
# Format: party[name] = GuildCreator.Member(name, lvl, ATK, DEF, SPD)
def individual(guild, quest):
    new_party = {}
    party_max = quest.size
    print(quest.diff)


    # randomly choose party size and hope the members are good enough
    party_size = randint(1, party_max)   
    print("\nThe party size will be: ", party_size)

    # randomly assign a guild member to the party2
    for x in range(party_size):
        some_member = choice(list(guild))
        # print(str(guild[some_member]))
        new_party[some_member] = guild[some_member]

    return new_party


# *** Generates a list-type population of party compositions
def population(count, ):

    return 


# *** Determines the success rate (AKA fitness) of a party for a certain quest
def fitness(party, quest):
    Atk_avg = 0
    Def_avg = 0
    Speed_avg = 0
    SucessRate = 0

    #Finds avg Atk stat
    for member in party:
        Atk_avg += party[member].attack
    Atk_avg = Atk_avg/len(party)

    #Finds avg Def stat
    for member in party:
        Def_avg += party[member].defense
    Def_avg = Def_avg/len(party)

    #Finds avg Speed stat
    for member in party:
        Speed_avg += party[member].speed
    Speed_avg = Speed_avg/len(party)

    '''
    Bounty: atk, spd, def
    Escort: def, atk,spd
    Fetch: spd, atk, def
    '''
    if quest._type is "bounty":
       Def_avg = Def_avg/2
       Speed_avg = Speed_avg/3
       PartyPoints = Atk_avg + Def_avg + Speed_avg
       SucessRate = (PartyPoints/quest.diff)*100
       return SucessRate
    
    if quest._type is "escort":
       Atk_avg = Atk_avg/2
       Speed_avg = Speed_avg/3
       PartyPoints = Atk_avg + Def_avg + Speed_avg
       SucessRate = (PartyPoints/quest.diff)*100
       return SucessRate
    
    if quest._type is "fetch":
       Atk_avg = Atk_avg/2
       Def_avg =Def_avg/3
       PartyPoints = Atk_avg + Def_avg + Speed_avg
       SucessRate = (PartyPoints/quest.diff)*100
       return SucessRate


# *** Find average success rate for all party compositions (used for comparison)
# def grade(population, target):

#     return avg
    

# *** Bulk of the genetic algorithm
# def evolve(population, target, ):

#     # randomly add other parties to promote genetic diversity

            
#     # mutate some parties by replacing random party members

    
#     # crossover two (parent) parties to create a better (child) party composition

#     return parents


# *** Main function 
if __name__ == "__main__":

  population = 100

  # Builds the guild with random guild members of varying stats
  guild = GuildCreator.generate()
  for member in Main.guild:
      print(str(Main.guild[member]))
  # print('\n')

  # Creates the quest for which a party will be assembled for
  # title, _type, diff, size = QuestCreator.create_quest()
  # questBoard[title] = QuestCreator.Quest(title, _type, diff, size)
  # for post in questBoard:
  #     print(questBoard[post])

  # Runs the genetic algorithm until a suitable party is made for each quest
  # for quest in questBoard:
  #     final_gen = sorted(evolve(guild, questBoard[quest]), key=Individual.fitness, reverse=True)
  #     best_party = final_gen[0]