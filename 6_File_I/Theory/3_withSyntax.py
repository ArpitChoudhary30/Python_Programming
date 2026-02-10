with open("/Users/arpitsingh/Desktop/Python_Programming/6_File_I/O/demo.txt", "r") as f:
    data = f.read()
    print(data)

#with function automatically closes the file so there is no need to write the close function