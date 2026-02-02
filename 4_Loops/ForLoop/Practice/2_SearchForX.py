#Search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

num = int(input("Enter the number to search:")
          )
for val in tup:
    if(val == num):
        print(tup.index(val)) #gives only the first occurrence of the element
        break
else:
    print("Element not found!")