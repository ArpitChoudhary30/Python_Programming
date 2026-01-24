num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if((num1 >= num2) and (num1 >= num3)): # if this condition fails, this implies num1 is not the greatest.
    print("The greatest of the three is:", num1)
elif((num2 >= num3)):
    print("The greatest of the three is:", num2)
else:
    print("The greatest of the three is:", num3)