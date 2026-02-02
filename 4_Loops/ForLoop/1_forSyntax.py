#for loop is used for sequential traversal

nums = [1, 2, 3, 4]

for val in nums:
    print(val)


tup = (1, 2, 3, 4, 5, 6, 7)

for val in tup:
    print(val)


string = "ApnaCollege"

for char in string:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else: #tasks which need to be done on full completion of loop are written in 'else' inside for loop
    print("End")
#this 'else' condition will only run when the loop runs completely without hitting the 'break/continue' statements.