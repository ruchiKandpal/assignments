income=int(input("Enter your salary here"))

tax=0
#standard deduction 
if(income>=50000):
    income=income-50000
#80C deduction 
if(income>=150000):
    income=income-150000

#tax is calculated below
if(income>=0 and income<=250000):
    tax=0
    print(tax)

elif(income>250000 and income<=500000):
    tax=(5/100*(income-250000))
    print(tax)

elif(income>500000 and income<=750000):
    tax=12500+(10/100*(income-500000))
    print(tax)

elif(income>750000 and income<=1000000):
    tax=37500+(15/100*income-750000)
    print(tax)

elif(income>1000000 and income<=1250000):

    tax=75000+(20/100*(income-1000000))
    print(tax)
    
elif(income>1250000 and income<=1500000):
    tax=125000+(25/100*(income-1250000))
    print(tax)

elif(income>1500000):
    tax=187500+(30/100*(income-1500000))
    print(tax)

elif(income<0):
    print("Invaid input")
    