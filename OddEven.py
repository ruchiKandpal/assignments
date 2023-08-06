oddN=0
evenN=0


number = [2,4,5,6,3,5,6,7,8,9,0,1,45,67,89,12,34,32,35,67,87,9,5,4,3,2,3,4,6,0]

for i in range(0,len(number)):
    if(number[i]>=2 and number[i]%2==0):
        evenN=evenN+1
    if(number[i]>=2 and number[i]%2!=0):
        oddN=oddN+1

print("No. of even numbers =",evenN)
print("No.of odd numbers =",oddN)



        
