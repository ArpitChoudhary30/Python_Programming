#this function will create a new file
def create_new_file() : 
    f = open("practice_for_2.txt", "w")
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
    f.close()

#creating a function to look for the word's line number
def check_for_line(): 
    word = "learning"
    data = True
    line_number = 1 #indicates the initial line number
    
    with open("/Users/arpitsingh/Desktop/Python_Programming/practice_for_2.txt", "r") as f:
        while data: #this condition remains true until there is a valid value in it. Becomes False if there is an empty string
            data = f.readline()
            if(word in data):
                print(line_number)
                return
            line_number+= 1

    return -1

check_for_line()