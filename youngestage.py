ruchi=int(input("Enter Age1 age here"  ))

dushyant=int(input("Enter Age2 age here  "))

monika=int(input("Enter Age3 age here  "))

tanmay=int(input("Enter Age4 age here"))

if(ruchi<dushyant or ruchi<monika or ruchi<tanmay):
    print("Age1 is the youngest of all  ")

elif(dushyant<ruchi or dushyant<monika or dushyant<tanmay):
    print("Age2 is the youngest of all")

elif(monika<ruchi or monika<dushyant or monika>tanmay):
    print("Age3 is the youngest of all  ")

elif(tanmay<ruchi or tanmay<dushyant or tanmay<monika):
    print("Age4 is the youngest of all  ")

else:  
    print("Invalid input")




