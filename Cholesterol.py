
LDL = int(input("What is your LDL Cholesterol Level? "))
HDL = int(input("what is your HDL Cholesterol Level? "))
TRI = int(input("What is your TRI Cholesterol Level? "))
Total_Cholesterol = (LDL+HDL+TRI)


if LDL < 100:
    print ("Your LDL is Good ")
elif (LDL > 100) and (LDL < 130):
    print ("Your LDL is Borderline ")
else :
    print("Your LDL is Bad ")

if HDL > 60:
    print ("Your HDL is Good ")
elif (HDL >= 50) and (HDL <= 60):
    print("Your HDL is Borderline")
else :
    print ("Your HDL is Bad ")

if TRI <150:
    print ("Your Triglycerides are good ")
elif (TRI >= 150) and (TRI <=200):
    print ("Your Triglycerides are Borderline ")
else :
    print ("Your Triglycerides are bad ")

if Total_Cholesterol < 200:
    print ("Your cholesterol levels are good ")
elif (Total_Cholesterol >= 200) and (Total_Cholesterol <= 240):
    print ("Your cholesterol levels are borderline ")
else:
    print ("Your cholesterol levels are bad ")


