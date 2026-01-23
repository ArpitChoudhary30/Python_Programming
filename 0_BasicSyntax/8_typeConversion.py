a = 2 #int
b = 4.3 #float

sum = a + b #Explicit Conversion -> float -> python automatically converts 'int' into 'float' as float is a more superior value => implicit conversion
# => sum = flaot value = 6.3

print(sum)

c = "2" #string
d = 4.25 #float
e = float(c) # float -> explicit type conversion -> manually done

# sum1 = c + d #invalid operation -> as str can not be added to a float number
sum2 = d + e # 6.25
print(sum2)

# f = int("Arpit") #TypeCasting won't happen here as the right datatype cannot fit into the other one.

g = 3.14
g = str(g)

print(type(g))
print(g)