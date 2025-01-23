#writing files
print("writing a file in Python")

print("-----------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

print("-----------------------------------------")

a = open("demo.txt", "a")
a.write("\nHere is a another line in our text file")
a.close()

#this apends a new line to the text file 

print("-----------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)
    a.close()

    #this opens the text file with the appended line

print("-----------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)


a= open("demo.txt", "w")
a.write("What has happened now?")
a.close()

#the w above overwrites what is in the file :) 

print("-----------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)


print("-----------------------------------------")


y = open("DaveFile.txt","x")

print("-----------------------------------------")




    
          



