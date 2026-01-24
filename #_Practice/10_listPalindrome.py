# WAP to check if a list contains a palindrome of elements.

list1 = [1, 2, 3, 2, 1]
check_list1 = list1.copy()
check_list1.reverse()

if(list1 == check_list1):
    print("The given list contains a palindrome of elements.")
else: 
    print("Not a palindrome of elements.")

list2 = [1, "abc", "abc", 1]
check_list2 = list2.copy()
check_list2.reverse()

if(check_list2 == list2):
    print("The given list contains a palindrome of elements.")
else:
    print("The given list does not contain a palindrome of elements.")