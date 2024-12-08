a = input("Do you have any Medical conditions Y/N")
b = int(input("What percentage attendance do you have "))
if (a == "Y" or a == "y"):
    print("You can take the exam")
    
else:
    if (b > 75):
        print("You can take the exam")
    else:
         print("You cannot take the exam")
    

