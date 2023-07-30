income=int(input("Enter your salary here"))
tax=0
if(income>=0 and income<=250000):
    tax=tax+0
    print(tax)
elif(income>250000 and income<=500000):
    tax=tax+(5/100*income)
    print(tax)
elif(income>500000 and income<=750000):
    tax=tax+(10/100*income)
    print(tax)
elif(income>750000 and income<=1000000):
    tax=tax+(15/100*income)
    print(tax)
elif(income>1000000 and income<=1250000):

    tax=tax+(20/100*income)
    print(tax)
elif(income>1250000 and income<=1500000):
    tax=tax+(25/100*income)
    print(tax)
elif(income>1500000):
    tax=tax+(30/100*income)
    print(tax)
elif(income<0):
    print("Invaid input")
    