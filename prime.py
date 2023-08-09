def prime(n):

    isprime=True

    if(n==0 or n==1):
        isprime=False
        return isprime
    a=2
    while(a<n):
        if(n%a==0):
            isprime=False
            break
        a=a+1
    return isprime

number=[4,7,9,1,2,3,44,5]

for i in range(0,len(number)):
    if(prime(number[i])==True):
        print(i)

