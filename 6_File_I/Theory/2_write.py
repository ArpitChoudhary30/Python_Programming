f = open("/Users/arpitsingh/Desktop/Python_Programming/6_File_I/O/demo1.txt", "w")
f1 = open("/Users/arpitsingh/Desktop/Python_Programming/6_File_I/O/demo1.txt", "a")

f.write("I will to complete this lecture today!")
f1.write("\nThen I will complete the rest of my tasks.")

f.close()

"""
What "w" does is that it completely overwrites the file, meaning, it firstly deletes the complete previous file content and then write the new one.

What "w" actually does (in file I/O)
When you open a file in write mode "w" (in C, C++, Python, etc.):

1. If the file already exists
The file is truncated to length 0 immediately.
This happens at open time, not when you start writing.
All previous content is irreversibly lost.

2. If the file does not exist
A new file is created.

3. After opening
Any write operation starts from the beginning of the file.


WHAT "a" DOES:
"a" (APPEND) keeps the file's current content and then add the new content at its end.

-> If a file is opened in write or append mode, and it does not exist, then a new file is automatically created.

WHAT "r+" DOES?
"r+" allows read and write. It overwrites the entered content over the existing content without deleting the entire previous content.
"""