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
   
