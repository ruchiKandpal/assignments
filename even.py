number=int(input("Enter the rannge you want "))
sum=0
a=1
while(a<=number):
    if(a%2==0):
        sum=sum+a
    else:
        sum=sum+0
    a=a+1
print(sum)
