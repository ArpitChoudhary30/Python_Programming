def print_list(lst):
    for item in lst:
        print(item, end = " ") #by default, on giving comma in 'print' function it prints the item on next line, but by defining end = " ", the items are printed on the same line

cities = ["Gurugram", "Chennai", "Lucknow", "Jaipur", "Mumbai", "Amritsar"]
print_list(cities)