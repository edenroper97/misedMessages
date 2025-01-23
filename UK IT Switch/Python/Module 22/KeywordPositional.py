def greet(name, msg = "How are you today?"):
    print("Hey",name + "," + msg)

#2 keyword arguments

greet(name="Dave",msg = "How do you do?")
print("-------------------------------------------------")

#out of order arguments

greet(msg="How do you do?", name="Dave")
print("-------------------------------------------------")

#1 positional, 1 keyword

greet("Dave", msg = "How do you doing?")
print("-------------------------------------------------")

greet("Dave")


    
