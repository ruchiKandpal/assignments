

"""
n=int(input("Enter a number:  "))

while(n>0):
   print(chr((n%10)))
   n=n//10
""""""
"""
def convert(number):
    if number==0:
        print("Zero")
        return
answer=" "
number=int(input("Enter a number here:  "))
while(number>0):
    answer=number%10
    
    convert(answer)
    print(answer)
    number=number//10




