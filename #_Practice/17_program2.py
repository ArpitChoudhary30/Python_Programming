#wap to segregate upper case and lower case letters in user defined string.

string = input("Enter the string: ")

for i in string:
    if(i.isupper()):
        print("upper: ", i)
    else:
        print("Lower: ", i)