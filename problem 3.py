#alex Feliciano
#10/09/2020
#a record that tells you what track are you on 
# track is the funcation to fine what track are you on
#start where the track is starting from
#skip is telling the function how many track you want to skip
def track(Start,skip):
    return (Start + skip)%12
Start = int(input("what track are you on:"))
skip =int(input("how many track do you want:"))
print ("your on track:",track(Start,skip))
