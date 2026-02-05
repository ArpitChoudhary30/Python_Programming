#Function : Block of statements that perform a specific task.
"""
FUNCTION SYNTAX:
function_name(para1, para2):
    #some work
    return val
"""

def cal_sum(a, b): #function definition
    sum = a + b
    return sum

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(cal_sum(a, b)) #function call -> passes arguments