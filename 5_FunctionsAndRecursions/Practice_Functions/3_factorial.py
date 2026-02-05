def factorial_of_n(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    
    return factorial

n = int(input("Enter the number: "))
print(factorial_of_n(n))