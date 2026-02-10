# A built-in data type that lets us create immutable sequence of values.

tuple = (1, 2, 3, 4)
print(type(tuple))

print(tuple[3]) #prints element at index 3 = 4

#values can not be assigned in a tuple

#tuple[3] = 7 # invalid operation as item assignment is not supported in tuple
#print(tuple)

tup = ()
print(tup)
print(type(tup))

tup1 = (1) #considered an integer data type
print(type(tup1))

tup2 = (1,) # use a comma to make it a tuple
print(type(tup2))