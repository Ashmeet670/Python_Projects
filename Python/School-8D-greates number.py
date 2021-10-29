number1 = float(input("Enter the first number "))
number2 = float(input("Enter the second number "))
number3 = float(input("Enter the third number "))

if(number1> number2 and number1 > number3):
                greatest = number1

if(number2 > number1 and number2 > number3):
                greatest = number2

if(number3> number1 and number3 > number2):
                greatest = number3


print("Number 1 is ", number1)
print("Number 2 is", number2)
print("NUmber 3 is", number3)
print("The greatest number is", greatest)


                                
