#Reading Files

print("Reading Files")
print("\n")
a = open("demo.txt", "r")
print(a.read())
a.close()


#Reading a file by line

print("Reading Files - Readline")

a = open('demo.txt',"r")
print(a.readline())
a.close()


#reading a ceartain amount of characters
print("Reading File Characters")
a = open('demo.txt',"r")
print(a.read(7))
a.close()


print("Reading Files - 'With'")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)
    

  
