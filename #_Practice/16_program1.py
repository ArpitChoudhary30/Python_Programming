#wap to print prime numbers and armstrong numbers upto range 1000.
#also print a number which is both prime and armstrong.

for i in range(2, 1001) :
    check = True

    for j in range(2, i):
        if(i % j == 0):
            check = False
    
    if(check == True) :
        print(i)


num = int(input("Enter a number: "))

count = len(str(num))
sum = 0
