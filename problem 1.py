#Alex feliciano
#interior angles finder
#10/09/2020
#the interior angle
#n is the number of sides of the polygon
def findAngle(n):
    interiorAngle = int((n-2)*180/n)
    return interiorAngle
    #displaying the input
n=10
print("Interior angle:",findAngle(n))
    #driver codeprint
    # Function calling
findAngle(n)
    # Python3 program to find  
