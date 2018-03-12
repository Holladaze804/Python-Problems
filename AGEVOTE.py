Age = int(input("How old are you? "))
Citizen = "Y"


if Age>=18:
    if Citizen =="Y":
        print ("You can vote in the USA")
    else:
        print("Sorry, only US citizens can vote")
else:
    print("You are too young to vote")
    
