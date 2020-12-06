#alex Feliciano
#11/3/2020
#lab activity 6
import random
def x():
#A function that uses a for loop to print 10 random integers between 25 and 35
    for x in range (10):
        print (random.randint(25, 35))
#A function that takes a list as a parameter and returns a random element from that list
def color():
    color = ["red","blue","yellow"]
    print(random.choice(color))
#A function that returns a random odd integer between 0 and 100
   
def n():
    for n in range(20):
        odd=random.randint(0,100)
        if odd%2 == 1:
            print(odd)
            break 

x()
color()        
n()
#A function that calculates the Pythagorean theorem using functions found in the math module.
# Python3 program for hypot() function  
  
# Import the math module 
import math 
  
# Use of hypot function 
print("hypot( x, x) : ", math.hypot( x,x )) 
