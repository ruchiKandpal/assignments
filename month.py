month=input("Enter the name of the month  ")

if(month=="january"or month=="January"or month=="march"or month=="March"or month=="may"or month=="May"or month=="July"or month=="july"or month=="August"or month=="august"or month=="October"or month=="october"or month=="December"or month=="december"):
    print("No.of days=31")

elif(month=="April" or month=="april" or month=="june" or month=="June" or month=="september" or month=="September" or month=="Novemebr" or month=="november"):
    print("No.of days=30")

elif(month=="February" or month=="february"):
    print("No.of days ==28 or 29")

else:
    print("Wrong Input")
