f = open("/Users/arpitsingh/Desktop/Python_Programming/6_File_I/O/demo.txt", "r")

data = f.read() #reads the entire file
print(data)
print(type(data))

f.seek(0) #this moves the cursor back to the starting point of the file

data1 = f.read(5) #will read only the first 5 characters
print(data1) #here this prints nothing => empty space
print(type(data1))

f.seek(0)

line1 = f.readline()
print(line1) #this prints all the characters of the first line. Also there is an "\n" which the code reads and prints an empty line along with it
#this readline() moves the cursor to the starting of second line after the completion of first line.

line2 = f.readline()
print(line2)

f.close()

"""
'data1' prints nothing because on reading the complete file by 'data', the file pointer moves to the end of file
which has nothing. So, first the cursor needs to be moved back to the starting and then only the file can be read again.

Every read/write happens at the current offset and advances it.
Nothing resets unless you explicitly reset it.
"""