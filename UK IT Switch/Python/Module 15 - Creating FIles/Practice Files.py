
#q1 below is hashed out to allow x below to run for part 2
#as practice exists you can't run it twice
#it will lead to an error


#x= open("PracticeFile.txt", "x")
#x.close()

#x = open("PracticeFile.txt", "a")
#x.write("Eden Stuart Christie Roper" '\n')
#x.write("Eden is 26 years old" '\n')
#x.close()

#x = open("PracticeFile.txt","r") 

#print(x.read())
#x.close()
   
print("---------------------------------------------")

#created file here
x = open("MyNewFile.txt","x")
x.close()

#opened the file and appended
x = open("MyNewFile.txt","a")
#added a while loop which is incremented
b = 1
while b < 4:
    x.write("yo mama fat" + str(b) + '\n') #turned it into a string
    b += 1
x.close()#closed the file

#opened the file here to read, assigned it and read it in IDLE 
x = open("MyNewFile.txt", "r")
print(x.read())
x.close()





         


