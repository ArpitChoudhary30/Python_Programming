#Search for a number x in this tuple using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tuple_ex = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

num = int(input("Enter the number to search for: "))

i = 1
while i < len(tuple_ex):
    print("Found at index:", tuple_ex.index(num))
    break
    i+= 1