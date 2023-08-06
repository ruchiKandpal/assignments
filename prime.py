number=[2,3,4,19,5,8,23,10,22,335]

prime=True
a=2
while(a<len(number)):
    if(number%a==0):
        prime=False
        break
    a=a+1
if(prime==True):
    print(number)   
