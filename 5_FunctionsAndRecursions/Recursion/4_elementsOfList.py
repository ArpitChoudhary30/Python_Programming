def print_list(lst, idx = 0):
    if(idx == len(lst)):
        return
    print(lst[idx], end = " ")
    print_list(lst, idx+1)


lst = [1, 2, 3, 4, 5, 6]

print_list(lst)