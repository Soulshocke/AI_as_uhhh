import GuildCreator
import QuestCreator
from Guildmaster import individual as party_create
from Guildmaster import fitness as PartySuccess
import random

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
print("oooooooooossssssssssssssssssssssssssssssssssssssssssssssooooo++++++++//:---\n\
oooooooooooooooooooooooooosssssssssssooossoo+/::::::::::/++oo+++/////---::/\n\
++++ooooooooooooooooooooooooooooooooosso/:::::::::::-:::::::/+/:--:////////\n\
/+++++++++++++++++++oooooooooooooooso/:::::::-------:/+oooooo+:/++///++++/+\n\
:/:-:::////++++++++++++++++ooo+++oo:::::::::::--:---:oohhyysoo+::/+++o++++o\n\
++///:::::://--::::::/+///:---::o/:::-----:://+/:::::/+hhhhhhy+:--:+oo+++os\n\
oooo+++++/+++////////++:.........:/::-----:+ooo+::::-::yhhhhhhhyo/::/o++osy\n\
sosss/:-...-:/ooooo+oo-...........::-----:oooo/:::::-::hhhhhhhhhhhyo/:oosyy\n\
ooso-.........:oooos+/::/++/::-----/::-:-:++/:----:+shddhhhhhhhhhhhhhyossyh\n\
oso/-/osso:----:+hyyo-./oys+.`....-:::-::::::--::+hmmmmmhhhhhhhhhhhhhhhhhhh\n\
osy/`-/+/-`````odmmdy:``...```````:::----------/ymmmmmddhhhhhhhhhhhhhhhhhhd\n\
ysdy.`````````/mmNNmss-`````````.::-:---------+dmmmmho/dhhhhhhhhhhhhhhhhhhh\n\
ssmms-``````-omNdmmmdyyo:.```..::::-::::----:+dmmmms:-/dhhhhhhhhhhhhhhhhhhy\n\
ssmmmdhso/:odmmNmddddddmdy://::::::::+o+:---:dmmmms:--/hhhhhhhhhhhhhhhhhhyy\n\
ssyyyyyyyy:syhhhmdddddddds-+::::::::+oo+:---smmmmh:---ohhhhhhhhhhhhhhhhyyyy\n\
ssmmmmmmmd/+dddmmddddddddo-+::::::::+oo/---:dmmmm+:--:shhhhhhhhhhhhhhhhyyyy\n\
ssmNmNmmmds:hmmNNmddddddm::/::::::-:///:---+mmmmh:--::yhhhhhhhhhhhhhhhhyyyy\n\
ssmmmNNNNdh/ommmNNddddddd-o+:::::::::------ommmmy:---:hhhhhhhhhhhhhhhhhhyyy\n\
ssmmmmNNNdyo:dmmNNmdddddy-yo::::::::------:ommmms:--::hhhhhhhhhhhhhhhhhhhhh\n\
oshhhhhhdhss:odhddmddddds-dy::::::::-------+mmmmy:---+hhhhhhhhhhhhhhhhhhhhh\n\
osdddddddhsss:yhhhdmdddm+:dd/:::::::-------:dmmmd::--shhhhhhhhhhhhhhhhhhhhh\n\
ssmNNmmNNdyoh+oNmmNNdddd//dds::::::::-------ymmmmo:::hhhhhhhhhhhhhhhhhhhyhd\n\
ssmmNNNmNdyohh:hmNNmmddd/+ddd/:::::::-------/dmmmh:-:hhhhhhhhhhhhhhhhhhhhdd\n\
osmNNNNNNdyohmo/mNNNNmdd:+ddds:::::::--------ommmms:+hhhhhhhhhhhhhhhhyhhdhh\n\
osmmNNmNNdyohmm+omNNNmdd:+dddd+::::::---------smmmmsyhhhhhhhhhhhhhhhhhhhyss\n\
oohddhdhdhsoyddh/ydddydd/+ddhy+//////::--------odmmmdhhhhhhhhhhhhhhhhhhosyh\n\
oohddhhhhysoyhhhh/so++os//y+:::::::::/:---------+hmmhhhhhhhhhhhhhyhhhhooyhm\n\
osmNNmmmmdyoymmmy/-....-----------:::::::::::::::+yhhhhhhhhhhhhhhhhddyo+ydN\n\
oomNNNNNNdyoydy/-....................------:::++++++ohhhhhhhhhhhhhddhyoohdN\n\
oommmNyosoo//:...............................-+/+++++yhhhhhhhhhhhddhhyoohdN\n\
oommmm/.........---------.........``...``````.++++++shhhhhhhhhhdhddhyyooyhh\n\
ysdmmmds+::-:/o+---....--......````````....-+ss++ssyhhhhhhhhhhhhhhhyssoosyy\n\
Nmhyyyyyyyyssyyy-..```...-:+oooooooooossyyyhhs++shhhhhhhhhhhhhhhhhhhddsohdN\n\
NMMNNNmmmmdosdmmmyo+++oys++yhhddddddddddhhhhs++shhhhhhhhhhhhhhhhhhhyyhhyhdN\n\
dMMMMMNNNmdssmmmdhyhhyhdyoohhhdmddddddhhhhyo++shhhhhhhhhhhhhhhhhhhhyyyyhhdN\n\
hmNNMMMMNNNhydhhyyhyyhdhy+ohhhhmddddhhhhhyo++shhhhhhhhhhhhhhhhhhhhhyyhhhhhd\n\
hmddmmNMMMNmhyyyhhhyyhdhy+ohhhhdddhhhhhhyo+oyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhy\n\
hmmmmddmNNdhyyyyyyyyhdhhho+yhhhhhhhhhhhs++oyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyy\n\
hdddddmmmhhhhyyyyyhyhhhhho+ohhhdhhhhhyo+oshhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyy\n\
dhsyhdddhhhhyyyyyyhhdhhhhyo+shhdhhhyo+++yhhhhhhhhhhhhhhhhhhhhhhdhhhhhhhhhyy\n\
hhhhyhhhhhhhhhyyyyhhdhhhhho+osdhhys+++shhhhhhhhhhhhhhhhhhhhhhhdhhhhhhhhhhyy\n\
yyyyyyyyhhyyyyyyyyhdhhhhhhyo+oso+++osyhhhhhhhhhhhhhhhhhhhhhhhdhhhhhhhhhhhhy\n\
yyyyyyyyyyyyyyyyyyhdhhhhhhhyoo+++osyhhhhhhhhhhhhhhhhhhhhhhhhdhhhhhhhhhhhhhy\n")
print("Welcome Traveler. I am the GuildMaster of this here Guild")
print("My Name is A.I.")


print("Day %d" % DayCount)

while UserInput != 5:
    print("\nSo what would you like to do, Traveler?")
    print("")
    print("1. I would like to check on the status of the Guild Members ")
    print("2. I have a Quest that I'd like to post to the Board")
    print("3. I want to check the QuestBoard")
    print("4. Thats all for today. I'll be back tommorow")
    print("5. GoodBye this is the last time I'll be in this town \n")
    UserInput = input()
    UserInput = int(UserInput)
    
    if UserInput == 1:
       print("Here are all the stats and levels of each Guild Member")
       for member in guild:
           print(str(guild[member]))
       print('\n')
    
    if UserInput == 2:
       if len(questBoard) is not 1:
       	  print("\nAlright I'm just gonna need some specifications of the Quest:")
          title, _type, diff, size = QuestCreator.create_quest()
          questBoard[title] = QuestCreator.Quest(title, _type, diff, size)
          print("\nSo the quest you made is:\n")
          print(str(questBoard[title]))
          '''
          print("Party sent is:")
          for member in Quest1_Party:
              print(str(Quest1Party[member]))
          '''
       else:
          print("There are too many Quests on the board right now. Come back tommorow!")
    
    if UserInput == 3:
       print("\nHere are the Quests:\n")
       for Quests in questBoard:
           print(str(questBoard[title]))
       # print('\n')
           
    if UserInput == 4:
       #Makes sure the questBoard isnt empty
       if(len(questBoard) > 0):
          print("\nAlright see you tommorow, Traveler!")
          print("I will now send the best people for your quest...")
          #*****AI is called here (below only works for one quest atm)
          for Quest in questBoard:
            Quest1_Party = party_create(guild, questBoard[Quest])

          #Report of who is sent
          
          #Test Party
          # Quest1_Party['ayy'] = GuildCreator.Member('ayy', 12, 6, 3, 15)
          # Quest1_Party['lmao'] = GuildCreator.Member('lmao', 14,7, 1, 20)
          # Quest1_Party['mom'] = GuildCreator.Member('mom', 16,8, 2, 22)
          # Quest1_Party['fam'] = GuildCreator.Member('fam', 18,6, 2, 28)

          DayCount += 1
          ActiveQuest = 0
          print("############################################################\n")
          print("Day %d" % DayCount)
          print("Welcome back, Traveler!")
          #Goes through each quest in the Board and return the status
          for Quest in questBoard:
              SuccessRate = PartySuccess(Quest1_Party,questBoard[Quest])
              QuestStatus = PassOrFail(SuccessRate)
              print("I sent the party consisting of:\n")
              for member in Quest1_Party:
                  print(str(Quest1_Party[member]))
              print("\nto take on the quest: ", questBoard[Quest].title)
              print("They ",QuestStatus," with a SuccessRate of",SuccessRate,"%")
          #Clears QuestBoard
          Quest1_Party = {}
          questBoard = {}
       else:
         print("\nThe day can't end, Traveler, if we have no Quests on the Board.\n")  
    
    if UserInput is 5:
       print("\nAlright it was nice having you around. Feel free to come back!")
       print("Good luck in your Travels!\n")
       break