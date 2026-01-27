collection = {1, 2, 3, 4}

print(type(collection))
print(collection)

#Duplicate values are ignored and no error is shown
collection1 = {1, 2, 2, 3, 4}
#repeated values are stored only once, so it resolved to {1, 2, 3, 4}
print(collection1)

collection2 = {1, 2, 2, 3, "Hello!, World"} #no specific format of output as set is unordered
print(collection2)
print(len(collection2)) #duplicate values are not counted in length.

#EMPTY SET SYNTAX : 
null_set = set()
print(type(null_set))

collection = {} #empty dictionary