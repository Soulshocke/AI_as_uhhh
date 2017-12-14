import GuildCreator
import QuestCreator
from Guildmaster import evolve
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
print("Welcome Traveler. I am the GuildMaster of this here Guild")
print("My Name is A.I.")
print("NMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNmmNmNNmNNNNNNNNmmmmmmmmmmmmmmmmNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmddhhhhyyysssyyyyyyyyyyyyyyyyyyhhhhhhdddmmNNMMMMMMMMMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMMMMNNmddhyysssoo++////////+++++++ooooooooooosssyyhhdmmNNMMMMMMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMMMNmdhysoo++///::---.......--::::::::/:://////++ossyyhhhddmmNMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMMMMNNdyyo++:::----....``````.-.....-----::-://////////ooooosyyhmMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMMmhsso+/:::/:-:-:--.....``...`````..-..-:/+++o++++++o+++++///++odMMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMNyo/+////+/o+oo++++/:--....``````.....--::::-::-----:://+++////oyNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMdo/::/+o+++//+/:::/::---.````````............`.````.....-:://:/+smMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMh+::+//::-:----..`.....````````....-......````.```````.....-://+smMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMMh+::::-..-:....```.-.``...`````........```````.:/+++/.``...--:/oymMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMN+:-----.-/++ssso+oo+--...```````......```.:/+///:+soo/:/oo/---:ohNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMN+-:--/oo+:+yhyyyso//sh/.````````......-/yhs/-:oyddmmms-`.:so--:+hNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMmo:-+hs-`.smNMMMMMNmy--/::.``````...-:sddo.``omNMMMMMMMNs..:/-::+hNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMdo:-yy:.-yNMMMMNNMMMNh-.+y/.````...:yNm/:-.`/mNMMNmMMMMMNy:::-::+dNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMmo::sh+::dNMMM   MMMNm:`.:+-.`.`..:yds+:-.``+NMMMM   MMMNh+//-::+dNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMms:-+dyo/yNMMMMMMMMNdo-.-+y+.`.```:ydhyo/-``.sdNNMMMMMMNh++os-::odNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMdo/::ohdyssmNNMMNNmdoosydddo-.```..-/shmdyo/::sdmNNNNNms/+sdd:-:oyNMMMMMMMMMMMMMMMM\n\
MMMMMMMMMMMMMMMMMdo::-:+ydmddmNmmmddddmmdhs/--.```.....-/shmmmmmdmmmmNmyyhmmmy:-:+smNMMMMMMMMMMMMMMM\n\
NMMMMMMMMMMMMMMMMdo+-..-::oyyshhhyyso/:::-:-::-```.--.--::::+shhhhhhdddhyyys+:--:+odNMMMMMMMMMMMMMMM\n\
NMMMMMMMMMMMMMMMMdo+-......-...---.......-:::::-.`.-----:::------..-//----...-.-:/+hmMMMMMMMMMMMMMMM\n\
NMMMMMMMMMMMMMMMMho/..-...............-----::::--.----::-::--....``............-/:+yhmMMMMMMMMMMMMMM\n\
NMMMMMMMMMMMMMMMMdo:--........`........----:::--...-::::://::-.............-.---::+ysdNMMMMMMMMMMMMM\n\
NMMMMMMMMMMMMMMMMms/:.........`.........--::/::----::///++//:...........--.-.--::/+oshmMMMMMMMMMMMMM\n\
NMMMMMMMMMMMMMMMMNs+:--........-........-:/o+///++++ooooso+/----.........------::/++shmMMMMMMMMMMMMM\n\
NNNMMMMMMMMMMMMMMNy+:---.......---..-...---::/+oossssssyo+//::---........-------:/:+yhmMMMMMMMMMMMMM\n\
NNNNMMMMMMMMMMMMMMh+/:---......---..-...-----:://+++///://:::-----.......----::-://+yymMMMMMMMMMMMMM\n\
NMNNNMMMMMMMMMMMMMmo//:----..---..---------::-::----::://::::--------------:::::///osyNMMMMMMMMMMMMM\n\
mNNNNMMMMMMMMMMMMMMh+/:-------:-..-----/oossoooo+++osyyyyoo+/::--.---------:::::///sshNMMMMMMMMMMMMM\n\
mNNmmNMMMMMMMMMMMMMNs/:::----:--.+yyhsyyyydo-.:hs:-+dmdydNmmmNdhs+:------:::::::++oysdMMMMMMMMMMMMMM\n\
dmNmmmNMMMMMMMMMMMMMd+:::-:-::--/dNmd+/:-:/.`.-+:``.so:-/ysohMMMMMNs:--::::::///+ooyhNMMMMMMMMMMMMMM\n\
dmmmmmdmNMMMMMMMMMMMNh///:::/:-::+mmmh+:---..-:+:...s+-::yssmMMMMMNd:-:::::////+ooyhNMMMMMMMMMMMMMMM\n\
dmmmmddmmNMMMMMMMMMMMNy////:::::::smNMNNmdmmmmmNmddmNNmmNMMMMMMMNmd+::::://///+ssyhNMMMMMMMMMMMMMMMM\n\
ddmmddddmmmNMMMMMMMMMMNs+////::::::+ohmmhssoodyymmhddhhmmdNMMMMNms+::://///++ossydNMMMMMMMMMMMMMMMMM\n\
dmmmmddddmddNMMMMMMMMMMMdo+/////::::::/ydmdhhhyyhyosyooyhydmmdyhy/:::///+++ooyyhmMMMMMMMMMMMMMMMMMMM\n\
dddmmmddddmddmNMMMMMMMMMMmyo++++////:::::/ooyhyssyyyyhhhhyo+/::::::://++ooosyhmMMMMMMMMMMMMMMMMMMMMM\n\
ddmmmdddddmmdddmNNNMMNNNNNms+//+/////////:::::::////////:/::://////+++oossyyhdNMMMMMMMMMMMMMMMMMMMMM\n\
hddddddhddddhhddmmmmmmNNNNmds//////:://///////////////////+//+++++oosoossyyyymMMMMMMMMMMMMMMMMMMMMMM\n\
ddddddddddhdhhhdhdddmmmmNNNNmh+///////////+++++++/+////++++++ooossssyyyyyyyhmNNmNMMMMMMMMMMMMMMMMMMM\n\
hddhddmmdddddmdddhhdmmmmmNNNNdhs++/+syssoooooo+o++++++ooooossyysyyyhdddddhhmmmmmNMMMMMMMMMMMMMMMMMMM\n")

print("Day %d" % DayCount)

while UserInput != 5:
    print("\nSo what would you like to do, Traveler")
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
       	  print("\nAlright I'm just gonna need some specifications of the Quest")
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
          print("There are too many Quests on the board right now. Come back tommorow")
    
    if UserInput == 3:
       print("\nHere are the Quests:\n")
       for Quests in questBoard:
           print(str(questBoard[title]))
       # print('\n')
           
    if UserInput == 4:
       #Makes sure the questBoard isnt empty
       if(len(questBoard) > 0):
          print("\nAlright see you tommorow Traveler")
          print("I will now send the best people for your quest")
          #*****AI is called here (below only works for one quest atm)
          #Report of who is sent
          #Find Best party for each quest
          for Quest in questBoard:
              Quest1_Party = evolve(100, guild, questBoard[Quest])
          #Test Party
          # Quest1_Party['ayy'] = GuildCreator.Member('ayy', 12, 6, 3, 15)
          # Quest1_Party['lmao'] = GuildCreator.Member('lmao', 14,7, 1, 20)
          # Quest1_Party['mom'] = GuildCreator.Member('mom', 16,8, 2, 22)
          # Quest1_Party['fam'] = GuildCreator.Member('fam', 18,6, 2, 28)

          DayCount += 1
          ActiveQuest = 0
          print("############################################################\n")
          print("Day %d" % DayCount)
          print("Welcome back Traveler")
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
         print("\nThe day can't end Traveler if we have no Quests on the Board\n")  
    
    if UserInput is 5:
       print("\nAlright it was nice having you around. Feel free to come back")
       print("Good luck in your Travels\n")
       break