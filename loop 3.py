#Alex Feliciano
#10/28/2020
#this ask the user how many sides and makes it for them

import turtle      
wn = turtle.Screen()  
alex = turtle.Turtle()
 
sides = input ("Number of sides in polygon?"  )
length = input ("Length of the sides in polygon?" )
colorname = input ("Color of polygon?" )
fcolor = input ("Fill color of polygon?")
 
alex.color = (colorname)
alex.fillcolor = (fcolor)
 
for i in range(sides):
   alex.forward (length)
   alex.left (360 / sides)
