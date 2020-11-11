#alex feliciano
#11/09/2020
#import anything you need here

#Define any other functions you'll need here

#This function is called by main_game.
#This will control the whole section
#It'll need the player character as an input in order to interact with them

#this is the story (section 1)
def start():
    print("it was a cold night ,and the fog swept in from the forest and suddenly you hear big crash from near the bridge leading into town.")
    print("Lucifer is riding his motorcycle in the fog then hears a crash and starts.")
    print("heading over there and suddenly sees a person in the middle of the road crying. Type one of these 4 options.")
#this is the interaction with maria at the bridge
    print("ask what happen ")       
    print("keep driving ")
    print("kill her ")
    print("offer her a ride ")
    choice = input(">")
    if choice == "ask what happen":
        print("my family went over the bridge & they couldn't get out & i'm the only one that got away.")
    if choice == "keep driving":
        print("your heading into town knowing you left someone back there minus 10 points from your humanity bar.")
    if choice == "kill her":
            print("you basically lost the whole game restart goofyass")
    if choice == "offer her a ride":
        print("no i dont ride with stangers ,CREEPY MAN")
              
              
        
