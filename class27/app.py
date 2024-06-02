import os

# open is a function
# It is accepting two different arguments below:
# The first one is the name of the file
# the second argument represent the mode that you want the file to open.

file_with_names = open("folder/demo.txt", "r")

# print(file_with_names.read())

# readlines is a function
# print(file_with_names.readlines())

# Write to an existing file
# "a", "w"
# "a" = append
# "w" = write / overwrite an existing content in a file

dummyFile = open("dummy.txt", "a")
dummyFile.write("Hello World")
dummyFile.close()

# write to a new file using the "w" parameter
newFile = open("newFile.txt", "w")
newFile.write(" Hi, this is jenn!")
newFile.close()

# Create a new file
# "x"
# it will create a new file, and if the file already exists, it will throw an error
# The following line will through an error because this file exist already.
# anotherFile = open("another.txt", "x")

os.remove("dummy.txt")

# check if a specific file exist:
if os.path.exists("dummy.txt"):
    print("File exist")
else:
    print("File does not exist")
    

# It will give us an error if the file does not exist.
# os.rmdir("nameofthefolder")