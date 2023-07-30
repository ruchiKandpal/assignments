days=int(input("Enter the number of days you visited the library"))

charge=0

if(days>=0 and days<=5):
    charge=charge+(days*2)
    print(charge)
if(days>5 and days<=10):
    charge=10+(days-5)*6
    print(charge)
if(days>10 and days<=15):
    charge=40+(days-10)*4
    print(charge)
if(days>15):
    charge=60+(days-15)*5
    print(charge)

if(days<0):
    print("Invalid Input")
