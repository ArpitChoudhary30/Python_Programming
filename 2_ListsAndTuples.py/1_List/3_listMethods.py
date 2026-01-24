list = [2, 1, 3]

list.append(4) #adds one element at the end [2, 1, 3, 4]
print(list)

list.sort() #sorts in ascending order -> changes occur in the list itself
print(list)

list.sort(reverse = True) #sorts list in descending order -> valid even for characters.
print(list)

list1 = ["Litchi", "Banana", "Apple"]
list1.sort(reverse = True)
print(list1)
list1.sort()
print(list1)

list2 = [1, 4, 3, 7, 4]
list2.reverse() #reverses the list in its original variable
print(list2)

list2.insert(2, 5) #list.insert(idx, val)
print(list2)

list2.remove(4) #removes first occurrence of '4'
print(list2)

list2.pop(3) #removes element at the given index
print(list2)