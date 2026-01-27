# Only Tuple can be used as keys.

info = {
    "name" : "Arpit",
    "Subjects" : ["DMS", "DBMS", "Python"],
    "Age" : "21",
    1 : 99
}

info["name"] = "Chhotu"
info["Surname"] = "Jaat"

print(info)

print(type(info))

print(info["name"])
print(info["Surname"])
print(info["Age"])

null_dict = {} #empty dictionary
print(type(null_dict))

null_dict["name"] = "Vasu"
print(null_dict["name"])