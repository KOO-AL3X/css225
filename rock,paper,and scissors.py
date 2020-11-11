from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

def battle():
#im trying to make this go forever just to test it and what i used in class today
    while true: 
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("you both trade blows")
        elif player == "Rock":
            if computer == "Paper":
                print("you take damage !", computer, "covers", player)
            else:
                print("you attacked!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("you take damage!", computer, "cut", player)
            else:
                print("You attacked!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("you take damage", computer, "smashes", player)
            else:
                print("you attacked!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
        computer = t[randint(0,2)]







