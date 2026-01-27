collection = set()

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(2)
collection.add("Arpit")
collection.add((1, 2, 3))

print(len(collection))
print(collection)

# collection.remove(7) #no such element exists, so error

collection.clear()
print(collection)
print(len(collection))

new_set = {"Hello", "Arpit", "Coding", "Python"}
print(new_set.pop()) #pops element in random order