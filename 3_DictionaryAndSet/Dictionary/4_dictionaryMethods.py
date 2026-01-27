student = {
    "Name" : "Arpit Choudhary",
    "Section" : "B",
    "Subjects" : {
        "DMS" : 86,
        "DBMS" : 90,
        "Python" : 84,
    },
    "Age" : 21
}

# All these outputs will be returned in the form of tuples.

print(student.keys()) #prints all the keys on the outermost layer
print(student.values()) #prints all the values
print(student.items()) #prints all the (key,value) pairs
print(student["Name"]) #direct access -> will give error in case the given key is not present in the dictionary
print(student.get("Name")) #will return "None" in case the key is not present in the dictionary.
print(student.get("name1"))

student.update({"City" : "Alwar"})
print(student)

new_Dict = {"Roll_number" : "24BCON0246", "College" : "JECRC"}
student.update(new_Dict)
print(student)

#if, in a new dictionary, a key with the name in old dictionary is used, the compiler will overwrite the previous key instead of creating a new one.