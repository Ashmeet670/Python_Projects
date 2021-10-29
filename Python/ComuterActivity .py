number = input("Enter a number: ")

valueNumber = "false"

noneisalpha = "false"
noneisdigit = "false"

if number.isalpha():
    noneisdigit = "true"

elif number.isdigit():
    noneisalpha = "true"


if noneisalpha == "true" and noneisdigit == "false":
    l = int(number)
    valueNumber = "true"

else:
    print("The value you entered is/are not a digit")
    


if valueNumber == "true":
    
    if l % 2 == 0:
        print(number + " is an even number")

    else:
        print(number + " is an odd number")


