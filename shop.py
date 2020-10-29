#alex feliciano
#10/13/2020
#a corner store that has for items
#self checking out machine that would count you item
#tell you the money you owe 
def hi ():
    #cost of the items
    milk = 2
    eggs = 1
    meat= 3
    water=1
    #store clerk is saying
    print("i have water,milk,eggs,meat to sell:")
    #items that you want 
    a=int(input("how many milk do you want?:"))
    b=int(input("how many eggs do you want?:"))
    c=int(input("how many meat do you want?:"))
    d=int(input("how many water do you want?:"))
    #final price
    x=print(a*2+ b*1+ c*3+ d*1)
 
    #this is the last price for your food
    final_price = x
    #if it cost less then 20$you could buy it
if float(final_price)<20: 
    print("confirmed purchase")
else: #if it cost more then 20$ it would say you dont have enough money 
    print("you dont have enogh money ") 
