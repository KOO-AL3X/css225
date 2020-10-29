#player_actions.py


def check_play_again(user_input):
    #if you say yes this would make it say play again 
    if user_input == "yes":
        print("play again")
#if the uer say no it would say game over
#if you put something else other then yes or no it would say invaild input 
    elif user_input == "no":
        print("game over")
    else:
        print("invalid input!")
check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
    
      
