def product_of_two(a, b=2): #here '2' has been set the default value of 'b', in case no value is passed to 'b'
    product = a * b
    print(product)
    return product


product_of_two() #will throw an error as there is no argument passes to the function
product_of_two(5)

#product_of_two(a = 1, b) -> wrong syntax as Non-default argument is always written first.