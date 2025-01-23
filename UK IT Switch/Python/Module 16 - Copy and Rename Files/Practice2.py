print("Question 2:")

x = open("Question2.txt","x")
x.close()


a = open("Question2.txt","a")
a.write("Yo mama so fat\n")
a.write("She used to gangbang with the hebrews\n")
a.close()

import shutil
import os

shutil.copy("Question2.txt","Question2B.txt")

b = open("Question2B.txt","a")
b.write("\nYo moma so old")
b.write("\nshe rode to work on a dinosaur")
b.close()


y = open("Question2.txt","r")
print(y.read())
y.close()

print("-------------------------------------------------")

z= open("Question2B.txt","r")
print(z.read())
z.close()








