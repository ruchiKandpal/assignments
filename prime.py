def prime(n):
    isprime=True
    if(n==0 or n==1):
        isprime=False

    a=2     
    while(a<len(n)):
        if(a%2==0) :
            isprime=False
            return isprime
        a=a+1


number=[2,3,4,19,5,8,23,10,22,335]

print(prime(number))







"""
prime=True
a=2
while(a<len(number)):
    if(number%a==0):
        prime=False
        break
    a=a+1
if(prime==True):
    print(number)
    """   
#munhe kuch nahi aa ara h 
#sorry


