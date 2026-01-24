str = "i am studying python from Apna College"

print(str.endswith("ge")) #returns True if the string ends with the entered characters

print(str.capitalize()) # this will not affect the original string.
# capitalize() makes first letter capital and the rest into forced lowercase.

# to change the original string, we need to declare it in the original string
print(str)
str = str.capitalize()

print(str)

str1 = "I am studying python from ApnaCollege."

#replace() does not change the original string.
print(str1.replace("o","a")) # this will replace all the 'o's from the string with 'a' in the output string.

#using replace() we can replace a phrase also

print(str1.replace("python", "Java"))

print(str1)

print(str1.find("o")) # this will return the first index of the first occurrer
print(str1.find("q"))
# find() will return -1 if the character does not exist in the string.

print(str1.count("am")) # this will return the number of times the phrase or charcater exists in the string.