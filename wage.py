age=int(input("Enter your Age here  "))
sex=(input("Select your gender M,m,F,f  "))

wage=0

if(age>=18 and age<30):
    if(sex=="M" or sex=="m"):
        wage=wage+700
        print(wage,"per day")
    if(sex=="F" or sex=="f"):
        wage=wage+750
        print(wage,"per day")

if(age>=30 and age<=40):
    if(sex=="M" or sex=="m"):
        wage=wage+800
        print(wage,"per day")
    else:
        wage=wage+850
        print(wage,"per day")
if(age<18 or age>40):
    if(sex=="M" or sex=="m"):
        print("Invalid Age")
    if(sex=="F" or sex=="f"):
        print("Invalid Age")
    
