n=int(input("Enter a number here"))

if(n%2==0):
    print("This is divisible by 2")

if(n%3==0):
    print("This is divisible by 3")

if(n%4==0):
    print("This is divisible by 4")

if(n%2==0 and n%3==0):
    print("This is divisible by 6")

if(n%2==0 and n%3==0 and n%4==0):
    print("This is divisible by all of the above")
    
if(n%2!=0 and n%3!=0 and n%4!=0):
    print("This is divisible by none of the above")

