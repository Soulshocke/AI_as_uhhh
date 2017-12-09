import GuildCreator
import QuestCreator
import random


#Calculates Party's success rate
def PartySuccess(Party,Quest):
    Atk_avg = 0
    Def_avg = 0
    Speed_avg = 0
    SucessRate = 0
    #Finds avg Atk stat
    for member in Party:
        Atk_avg += Party[member].attack
    Atk_avg = Atk_avg/len(Party)
    #Finds avg Def stat
    for member in Party:
        Def_avg += Party[member].defense
    Def_avg = Def_avg/len(Party)
    #Finds avg Speed stat
    for member in Party:
        Speed_avg += Party[member].speed
    Speed_avg = Speed_avg/len(Party)
    '''
    Bounty: atk, spd, def
	Escort: def, atk,spd
	Fetch: spd, atk, def
	'''
    if Quest._type is "bounty":
       Def_avg = Def_avg/2
       Speed_avg = Speed_avg/3
       PartyPoints = Atk_avg + Def_avg + Speed_avg
       SucessRate = (PartyPoints/Quest.diff)*100
       return SucessRate
    
    if Quest._type is "escort":
       Atk_avg = Atk_avg/2
       Speed_avg = Speed_avg/3
       PartyPoints = Atk_avg + Def_avg + Speed_avg
       SucessRate = (PartyPoints/Quest.diff)*100
       return SucessRate
    
    if Quest._type is "fetch":
       Atk_avg = Atk_avg/2
       Def_avg =Def_avg/3
       PartyPoints = Atk_avg + Def_avg + Speed_avg
       SucessRate = (PartyPoints/Quest.diff)*100
       return SucessRate

#Determines whether or not the Party passes the quests   
def PassOrFail(Rate):
    Pass_Or_Fail = "failed"
    if (random.random()*100)<=Rate:
       Pass_Or_Fail = "passed"
    return Pass_Or_Fail



guild = GuildCreator.generate()
DayCount = 0
UserInput = 0
Quest1_Party = {}
questBoard = {}
QuestStatus = "none"
SuccessRate = 0
#Gives a user a list of item to do 
print("############################################################")
print("Welcome Traveler. I am the GuildMaster of this here Guild")
print("My Name is A.I.")
print("Day %d" % DayCount)

while UserInput != 5:
    print("So what would you like to do, Traveler")
    print("")
    print("1. I would like to check on the status of the Guild Members ")
    print("2. I have a Quest that I'd like to post to the Board")
    print("3. I want to check the QuestBoard")
    print("4. Thats all for today. I'll be back tommorow")
    print("5. GoodBye this is the last time I'll be in this town")
    UserInput = input()
    UserInput = int(UserInput)
    
    if UserInput == 1:
       print("Here is all the stats and levels of each Guild Member")
       for member in guild:
           print(str(guild[member]))
    
    if UserInput == 2:
       if len(questBoard) is not 1:
       	  print("Alright I'm just gonna need some specifications of the Quest")
          title, _type, diff, size = QuestCreator.create_quest()
          questBoard[title] = QuestCreator.Quest(title, _type, diff, size)
          print("So the quest you made is:")
          print(str(questBoard[title]))
          '''
          print("Party sent is:")
          for member in Quest1_Party:
              print(str(Quest1Party[member]))
          '''
       else:
          print("There are too many Quests on the board right now. Come back tommorow")
    
    if UserInput == 3:
       print("Here are the Quests:")
       for Quests in questBoard:
           print(str(questBoard[title]))
           
    if UserInput == 4:
       #Makes sure the questBoard isnt empty
       if(len(questBoard) > 0):
          print("Alright see you tommorow Traveler")
          print("I will now send the best people for your quest")
          #AI is called here
          #Report of who is sent
          '''
          #Test Party
          Quest1_Party['ayy'] = GuildCreator.Member('ayy', 12, 6, 3, 15)
          Quest1_Party['lmao'] = GuildCreator.Member('lmao', 14,7, 1, 20)
          Quest1_Party['mom'] = GuildCreator.Member('mom', 16,8, 2, 22)
          Quest1_Party['fam'] = GuildCreator.Member('fam', 18,6, 2, 28)
          '''
          DayCount += 1
          ActiveQuest = 0
          print("############################################################")
          print("Day %d" % DayCount)
          print("Welcome back Traveler")
          #Goes through each quest in the Board and return the status
          for Quest in questBoard:
              SuccessRate = PartySuccess(Quest1_Party,questBoard[Quest])
              QuestStatus = PassOrFail(SuccessRate)
              print("I sent the party consisting of:")
              for member in Quest1_Party:
                  print(str(Quest1_Party[member]))
              print("to take on the quest ", questBoard[Quest].title)
              print("They ",QuestStatus," with a SuccessRate of",SuccessRate,"%")
          #Clears QuestBoard
          Quest1_Party = {}
          questBoard = {}
       else:
         print("The day can't end Traveler if we have no Quests on the Board")  
    
    if UserInput is 5:
       print("Alright it was nice having you around. Feel free to come back")
       print("Good luck in your Travels")
       break
    
    
       

