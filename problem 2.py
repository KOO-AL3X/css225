#alex feliciano
#BMI calculator
#10/09/2020
#it takes height in inches and weight in pounds and uses it to find the bmi and return it
def bmi(height,weight):
    return weight/(height*height)*703
#the person hieght 
height = float(input("Input your height in inches: "))
#the persons weight
weight = float(input("Input your weight in pounds: "))
#solution 
print("Your body mass index is: ", bmi(height,weight))

