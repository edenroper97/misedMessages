#Fortmatting OutPut

salary = 44000
txt = "You make {} dollars a year"
print(txt.format(salary))


print("-----------------------------------------")



string = "Dave teaches {} {}."
print(string.format("cyber", "security"))

print("-----------------------------------------")

string = "David loves {} {}, and has {} {}."
print(string.format("cyber","security",14,"certifications"))

print("-----------------------------------------")

string = "David loves {}{}, and has {}{}."
print(string.format("kids","Cyber",7,"security"))


print("------------------------------------------")

string = "David loves {1} {3}, and has {2} {0}."
print(string.format("kids","Cyber",7,"security"))

print("------------------------------------------")

string = " Bob likes to play {act} and eat {1} {0}."
print(string.format("dogs","hot",act="games"))

print("--------------------------------------------")

print("Bob likes to play {act} and eat {1} {0}.".format("dogs","hot",act="games"))







