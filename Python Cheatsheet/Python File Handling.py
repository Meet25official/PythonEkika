# Read file

# Line by lice
"""
with open("myfile.txt") as file:
    for line in file:
        print(line)
"""

#With line number
"""
file = open('myfile.txt', 'r')
for i, line in enumerate(file, start=1):
    print("Number %s: %s" % (i, line))
"""

#String

#Write a string
"""
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))
"""

#Read a string
"""
with open('myfile1.txt', "r+") as file:
    contents = file.read()
print(contents)
"""

#Object

#Write an object
"""
import json
contents = {"aa": 12, "bb": 21}
with open("myfile2.txt","w+") as file:
    file.write(json.dumps(contents))

"""

#Read a string
"""
import json
with open('myfile2.txt', "r+") as file:
    contents = json.load(file)
print(contents)
"""

# Delete a File
"""
import os
os.remove('myfile.txt')
"""

# Check and Delete
"""
import os
if os.path.exists('myfile2.txt'):
    os.remove('myfile2.txt')
else:
    print("The file does not exist")
"""

#Delete Folder
"""
import os
os.rmdir('myfolder')
"""