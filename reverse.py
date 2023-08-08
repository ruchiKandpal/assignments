def convert(digit):
    if(digit==0):
        return("Zero")
    if(digit==1):
        return("One")
    if(digit==2):
        return("Two")
    if(digit==3):
        return("Three")
    if(digit==4):
        return("Four")
    if(digit==5):
        return("Five")
    if(digit==6):
        return("Six")
    if(digit==7):
        return("Seven")
    if(digit==8):
        return("Eight")
    if(digit==9):
        return("Nine")
"""  
number=int(input("Enter a number  "))

while(number>0):
    answer=number%10
    print(convert(answer))
    number=number//10
"""
number=int(input("Enter a number   "))

digits=[]

while(number>0):
    digits.append(number%10)
    number=number//10

digits.reverse()

for i in range(0,len(digits)):
    print(convert(digits[i]))
        

