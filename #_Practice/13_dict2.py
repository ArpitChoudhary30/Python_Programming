subjects = {}

subject_marks = int(input("Enter physics marks: "))
subjects.update({"Physics" : subject_marks})

subject_marks = int(input("Enter chemistry marks: "))
subjects.update({"Chemistry" : subject_marks})

subject_marks = int(input("Enter maths marks: "))
subjects.update({"Maths" : subject_marks})

print(subjects)