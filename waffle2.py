size=input("Select a size amongst S,s,M,m,L,l ")
bill=0

if(size=="S" or size=="s"):
    bill=bill+129
elif(size=="M" or size=="m"):
    bill=bill+159
elif(size=="L" or size=="l"):
    bill=bill+199
else:
    print("Invalid selection")


icecream=input("Want ice-cream with this yes or no ")

if(icecream=="yes"):
    if(size=="s"or size=="S"):
        bill=bill+20
    if(size=="M" or size=="m"):
        bill=bill+30
    if(size=="l" or size=="L"):
        bill=bill+50
else:
    bill=bill+0

cherries=input("Want some cherries with this yes or no")

if(cherries=="yes"):
    if(size=="S" or size=="s"):
        bill=bill+10
    if(size=="M" or size=="m"):
        bill=bill+15
    if(size=="l" or size=="L"):
        bill=bill+20
else:
    bill=bill+0

bag=input("Want a carry bag with this too yes or no ")

if(bag=="yes"):
    bill=bill+5
else:
    bill=bill+0

delivery=input("Do you want a home delivery for this order yes or no")
if(delivery=="yes"):
    bill=bill+14
    print(bill)

else:
    bill=bill+0
    print(bill)
