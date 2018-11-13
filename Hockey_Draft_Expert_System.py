#Creating an AI expert system that uses PyKnow to answer a question. 

#Hockey teams spend millions of dollars trying to determine if they should draft an 18 year old based on an attempt to project 
#their future skill and impact in the NHL. This expert system will allow you to determine which round you should draft a
#player based on 5 different criteria. Hockey drafts are typically much more complicated, but this will provide a starting point,
#because these are the 5 most important criteria for a hockey player. In the NHL there are 7 rounds of drafting.

#As this is just a basic expert system all leagues that prospects play in will be viewed as equal. 

#The 5 criteria will be as follows:
# 1. Hockey IQ (high medium low)
# 2. Skating (high medium low)
# 3. Best player on their line (Yes/No) - this is important for determining if players are being carried
# 4. Offensive Driver (high medium low)
# 5. Defensive Awareness (high medium low)

#while it makes sense that you would want to draft a player with the highest stats this in all rounds this is implied by
#telling it to draft in the first round. 

#This expert system allows you to put in the stats for the players, but states where players should be drafted based on
#priority of skills. For example the player could have "High" ratings in points 2 through 5, but if he has a low hockey
#IQ the program will tell you not to draft this player, as it views Hockey IQ as the most important stat for future success.
#Alternatively if the player has Medium hockey IQ, and low scores in every other category it will still tell you to try
#drafting them in the seventh round. Again it does this, because it believes that hockey IQ is the single most important 
#trait. In fact if the player has a hockey IQ of medium they will not be suggested to be drafted until the sixth round
#at the earliest. 
#Conversely a players ability to drive offense and/or defensive awareness is not as important and therefore a player
#with a medium skill set in both of these aspects (while having high scores in the remaining three categories) will be
#considered in the second or third round. 

#This program also differentiates the skillset based on if it is a forward or a defenseman. The first question asked is
#therefore for positioning. The above description of the priorities will therefore be affected by the position of the
#player. 
#Goalies will not be considered due to the unpredictably of drafting goalies.



import sys
from pyknow import *

#Create a function that determines if the answer is true or false
def T_F(variable):
    if(variable == "yes"):
        answer = True
    else:
        answer = False
    return answer

class Hockey_IQ(Fact):
    pass

class Skating(Fact):
    pass

class LineMate(Fact):
    pass

class Off_driver(Fact):
    pass

class Def_aware(Fact):
    pass

class Position(Fact):
    pass

class DraftRound(KnowledgeEngine):
    #drafting forwards
    @Rule(
        AND(
            OR(Position(positions = "forward"), Position(positions = "defense")),
            Hockey_IQ(hockey_iq = "high"),
            Skating(skating = "high"),
            LineMate(linemate = True),
            Off_driver(off_driver = "high"),
            Def_aware(def_aware = "high")))
    def first_f(self):
        print("Draft this player in the first round")
    
    @Rule(
        OR(
            AND(
                Position(positions = "forward"),
                Hockey_IQ(hockey_iq = "high"),
                Skating(skating = "high"),
                LineMate(linemate = True),
                Off_driver(off_driver = "high"),
                OR(Def_aware(def_aware = "high"), Def_aware(def_aware = "medium"))),
            AND(
                Position(positions = "defense"),
                Hockey_IQ(hockey_iq = "high"),
                Skating(skating = "high"),
                LineMate(linemate = True),
                OR(Off_driver(off_driver = "high"), Off_driver(off_driver = "medium")),
                Def_aware(def_aware = "high"))))
    def second_f(self):
        print("Draft this player in the second round")
    
  
    @Rule(
        OR(
            AND(
                Position(positions = "forward"),
                Hockey_IQ(hockey_iq = "high"),
                OR(Skating(skating = "high"), Skating(skating="medium")),
                LineMate(linemate = True),
                OR(Off_driver(off_driver = "high"), Off_driver(off_driver = "medium")),
                OR(Def_aware(def_aware = "high"), Def_aware(def_aware = "medium"))),
            AND(
                Position(positions = "defense"),
                Hockey_IQ(hockey_iq = "high"),
                Skating(skating = "high"),
                LineMate(linemate = True),
                OR(Off_driver(off_driver = "high"), Off_driver(off_driver = "medium")),
                OR(Def_aware(def_aware = "high"), Def_aware(def_aware = "medium")))))
    def third_f(self):
        print("Draft this player in the third round")

    @Rule(
        OR(
            AND(
                Position(positions = "forward"),
                Hockey_IQ(hockey_iq = "high"),
                OR(Skating(skating = "high"),Skating(skating= "medium")),
                OR(Off_driver(off_driver = "high"), Off_driver(off_driver = "medium")),
                OR(Def_aware(def_aware = "high"), Def_aware(def_aware = "medium"))),
            AND(
                Position(positions = "defense"),
                Hockey_IQ(hockey_iq = "high"),
                Skating(skating = "high"),
                OR(Off_driver(off_driver = "high"), Off_driver(off_driver = "medium")),
                OR(Def_aware(def_aware = "high"), Def_aware(def_aware = "medium")))))
    def fourth_f(self):
        print("Draft this player in the fourth round")

    
    @Rule(
        OR(
            AND(
                Position(positions = "forward"),
                Hockey_IQ(hockey_iq = "high"),
                OR(Skating(skating = "high"), Skating(skating="medium")),
                OR(Off_driver(off_driver = "high"), Off_driver(off_driver = "medium"))),
            AND(
                Position(positions = "defense"),
                Hockey_IQ(hockey_iq = "high"),
                OR(Skating(skating = "high"), Skating(skating="medium")),
                OR(Def_aware(def_aware = "high"), Def_aware(def_aware = "medium")))))
    def fifth_f(self):
        print("Draft this player in the fifth round")

    @Rule(
        AND(
            OR(Position(positions = "forward"),Position(position = "defense")),
            OR(Hockey_IQ(hockey_iq = "high"), Hockey_IQ(hockey_iq = "medium")),
            OR(Skating(skating = "high"), Skating(skating="medium"))))

    def sixth_f(self):
        print("Draft this player in the sixth round")
        
    @Rule(
        AND(
            OR(Position(positions = "forward"),Position(position = "defense")),
            OR(Hockey_IQ(hockey_iq = "high"), Hockey_IQ(hockey_iq = "medium"))))
    def seventh_f(self):
        print("Draft this player in the seventh round")
        
    @Rule(Hockey_IQ(hockey_iq = "low"))
    def DND_f(self):
        print("Do not draft this player")
        
         
system = DraftRound()
system.reset()

linemate_q = False

print("All rankings should be high medium or low")
position_q = input("What position does this player play? (Forward, Defense or Goalie) ").lower()
if(position_q == "goalie"):
    print("This expert system does not rank goalies due to their unpredictability! Pick a different player")
#elif(position_q == "forward" or position_q == "defense"):
else:
    hockey_iq_q = input("Rate the players hockey IQ: ").lower()
    skating_q = input("Ratethe players skating ability: ").lower()
    linemate_q = input("Is the player the best player on their line? (Yes or No)").lower()
    off_driver_q = input("Rate the player's ability to drive offense: ").lower()
    def_aware_q = input("Rate the player's defensive awareness: ").lower()
    
    system.declare(Position(positions = position_q), Hockey_IQ(hockey_iq= hockey_iq_q), Skating(skating= skating_q), 
             LineMate(linemate = T_F(linemate_q)), Off_driver(off_driver= off_driver_q), Def_aware(def_aware= def_aware_q))
    system.run()
#else:
#    print("You have made an error. Please try again!")
   
