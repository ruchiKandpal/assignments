a=int(input("Enter your amount here  "))

t=float(input("Enter time here  "))

interest=0


if(a>=0 and a<100000):

    if(t>=0 and t<1):
        interest=interest+((a*5*t)/100)
        print(interest)
    if(t>=1 and t<5):
        interest=interest+((a*6*t)/100)
        print(interest)
    if(t>=5 and t<10):
        interest=interest+((a*8*t)/100)
        print(interest)
    if(t>=10):
        interest=interest+((a*10*t)/100)
        print(interest)
    if(t<0):
        print("Invalid time entered")


if(a>=100000 and a<1000000):

    if(t>=0 and t<1):
        interest=interest+((a*10*t)/100)
        print(interest)
    if(t>=1 and t<5):
        interest=interest+((a*11*t)/100)
        print(interest)
    if(t>=5 and t <10):
       interest=interest+((a*13*t)/100)
       print(interest)
    if(t>=10):
        interest=interest+((a*15*t)/100)
        print(interest)
    if(t<0):
        print("Invalid time entered")


if(a>=1000000 and a<10000000):

    if(t>=0 and t<1):
        interes=interest+((a*15*t)/100)
        print(interest)
    if(t>=1 and t<5):
        interest=interest+((a*16*t)/100)
        print(interes)
    if(t>=5 and t<10):
        interest=interest+((a*18*t)/100)
        print(interest)
    if(t>=10):
        interest=interest+((a*20*t)/100)
        print(interest)
    if(t<0):
        print("Invalid time entered")


if(a>=10000000):

    if(t>=0 and t<1):
        interest=interest+((a*20*t)/100)
        print(interest)
    if(t>=1 and t<5):
        interest=interest+((a*21*t)/100)
        print(interest)
    if(t>=5 and t<10):
        interest=interest+((a*23*t)/100)
    if(t>=10):
        interest=interest+((a*25*t)/100)
        print(interest)
    if(t<0):
        print("Invalid time entered")

        
if(a<0):
    print("Invalid amount entered")




