def fact_n(n):
    if(n == 1 or n == 0):
        return 1
            
    return n * fact_n(n-1)


n = int(input("Enter the value of n: "))

print(fact_n(n))

# n! = n * (n-1)!