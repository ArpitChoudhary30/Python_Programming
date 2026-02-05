def currency_conversion(dollar):
    current = dollar * 92
    return current

amount = int(input("Enter the amount in $: "))

print(currency_conversion(amount))