test1 = int(input("What grade did you receive on test 1? "))
test2 = int(input("What grade did you receive on test 2? "))
test3 = int(input("What grade did you receive on test 3? "))
test4 = int(input("What grade did you receive on test 4? "))
testaverage = ((test1 + test2 + test3 + test4) / 4)

if testaverage >=90:
    print ("Your grade is A. Excellent job! ")
    print ("Your final average is",testaverage)

elif testaverage >=80:
    print("Your grade is B. Good work. ")
    print("Your final average is",testaverage)
    
elif testaverage >=70:
    print("Your grade is C. You passed the course. ")
    print("Your final average is",testaverage)

elif testaverage <70:
    print("Your grade is F. You failed the course. ")
    print("Your final average is",testaverage)
    


