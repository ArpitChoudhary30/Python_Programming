# Arithmetic Operators -> +, -, *, /, %, **
a = 7
b = 4

print(a+b) #addition operator
print(a-b) #subtraction operator
print(a*b) #multiplication operator
print(a/b) #division operator -> gives float answer by default even for integer numbers
print(a%b) #modulo operator -> gives the remainder when a is divided by b
print(a**b) #power operator -> gives the result when a is raised to the power of b

# RELATIONAL/COMPARISON OPERATORS -> ==, !=, >=, <=, >, <
c = 50
d = 20

print(c == d) #False
print(c != d) #True
print(c > d) #True
print(c < d) #False
print(c <= d) #False
print(c >= d) #True

#ASSIGNMENT OPERATORS -> =, +=, -=, *=, /=, %=, **=
e = 10

e+= 10; print(e) #20
e-=10; print(e) #10
e*=10; print(e) #100
e/=10; print(e) #10.0 -> gives float value by default
e%=10; print(e) #0.0 -> as 'e' becomes a float value after division operator
e**=10; print(e) #0.0

#LOGICAL OPERATORS -> and, or, not -> used on boolean values.
""" 
'not' operator reverses the original answer
'and' operator returns 1 if both the values are True
'or' operator returs false if both the values are False
"""
f = 50
g = 60

print(not False) #True
print(not (a>b)) #True

val1 = True
val2 = True
print("AND operator:", val1 and val2)

print("OR operator:", (f==g) or (f > g)) # False or False => False
print("OR operator:", (f==g) or (f < g)) # False or True => True

print("NOT Operator: ", not val1)