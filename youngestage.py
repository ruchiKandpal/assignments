age1=int(input("Enter Age1 age here"  ))

age2=int(input("Enter Age2 age here  "))

age3=int(input("Enter Age3 age here  "))

age4=int(input("Enter Age4 age here"))

if(age1<age2 or age1<age3 or age1<age4):
    print(age1, "is the youngest of all  ")

elif(age2<age1 or age2<age3 or age2<age4):
    print(age2, "is the youngest of all")

elif(age3<age1 or age3<age2 or age3<age4):
    print(age3, "is the youngest of all  ")

elif(age4<age1 or age4<age2 or age4<age3):
    print(age4,"is the youngest of all  ")

else:  
    print("Invalid input")




