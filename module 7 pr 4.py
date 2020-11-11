#alex feliciano
#11/10/2020
#lab 7
#problem four
import random
def archer():
    score =0
    score_card =[]
    arrow = 10
#Generate a random number between 0 and 10 to represent where on the target you managed to hit.
    while arrow > 0:
        target = random.randint(0,10)
        if target == 0:
            pass
#If the number is 0, you earn no points, but don't lose an arrow.
#if the number is 10, you got a bullseye! Increase your score by 20 points, then subtract 1 from your remaining arrows.
        elif target == 10:
            score +=20
            arrows -=1
        else:
            score += target
            arrow -=1
#Once you're out of arrows, print the final score and the score card.            
    print("final score is",score,"points")

            
archer()
