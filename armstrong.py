n=input("Enter a number here  ")

length=len(n)

n=int(n)
sum=0
x=n
while(n>0):
    sum=sum+(n%10)**length
    n=n//10

print(sum)



if(sum==x):
    print("Its an arm strong number")
else:
    print("Its not an arm strong number")
