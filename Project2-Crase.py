"""
File: Project2
Author: Cole Crase
This will allow the user to naviagte the liens of text in a file.
"""

fileName = input("Enter the file name: ")
f = open(fileName, 'r')
Counter = 0 
for n in f:
    if n:
        Counter += 1

print("The number of lines in this file is", Counter)
while True:
    number = int(input("Enter a line number or press 0 to quit: "))

    if number > 0 and number < Counter +1:
        print(f.readline)
    elif number == 0:
        print("The program is done.")
    
