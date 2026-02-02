n = int(input("Enter the value of n:"))

i = 1
fact = 1

for i in range(1, n+1):
    fact*= i
    print(fact)