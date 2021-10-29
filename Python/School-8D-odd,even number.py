number = input("Enter a number ")

numberIsValid = "false"

numberInt = 0

if(number.isdigit()):
    numberInt = int(number)
    numberIsValid = "true";
    
else:
        print(number + " is not a valid number")


if(numberIsValid == "true"):
    if(number % 2 == 0):
        print(number + " is a even number")
    else:
        print(number + " is a odd number")        



        
    
