import random
cnumber=random.randrange(1,101)
userinput=int(input("Enter your Number:-"))
if userinput>cnumber:
    print("Computer generated number:-",cnumber)
    print("Your number is too High")
elif userinput<cnumber:
    print("Computer generated number:-",cnumber)
    print("Your number is too low")
else:
    print("The Computer Generated number:-",cnumber)
    print("The User Given number:-",userinput,"are equal")
