"""
Create a new file "practice.txt" using python. Add the following data in it:
    Hi everyone
    we are learning File I/O
    using Java.
    I like programming in Java.

WAF that replaces all occurrences of "Java" with "Python" in above file.
Search if the word "learning" exists in the file or not.
"""

with open("/Users/arpitsingh/Desktop/Python_Programming/6_File_I/Practice/practice.txt", "r") as f:
    data = f.read() #using this I read the file practice.txt
    
new_data = data.replace("Java", "Python")
print(new_data) #this returns new data

with open("/Users/arpitsingh/Desktop/Python_Programming/6_File_I/Practice/practice.txt", "w") as f:
    data = f.write(new_data) #this overwrites the previous file with the new updations


word = "learning"
with open("/Users/arpitsingh/Desktop/Python_Programming/6_File_I/Practice/practice.txt", "r") as f:
    data1 = f.read()
    if(data1.find(word) != -1):
        print("Found")
    else:
        print("Not found")