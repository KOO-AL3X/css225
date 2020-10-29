#alex Feliciano
#10/28/2020
#iterates the integers from 1 to 50.
#For multiples of three print “Divisible by three” instead of the number
#and for the multiples of five print “Divisible by five”. 
for num in range(1,51):
    string = ""
    if num % 3 == 0:
        string = string + "Divisible by three"
    if num % 5 == 0:
        string = string + "Divisible by five"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)
