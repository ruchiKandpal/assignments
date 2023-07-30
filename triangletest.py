a=int(input("Enter the first side of triangle"  ))
b=int(input("Enter the second side of triangle" ))
c=int(input("Enter the third side of triangle" ))

if(a==b and b==c):
    print("Equilateral Triangle")
elif(a==b or b==c or c==a):
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")