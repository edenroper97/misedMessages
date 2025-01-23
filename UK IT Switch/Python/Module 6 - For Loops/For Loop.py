employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
for emp in employees:
    print(emp)


employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
if "Tammy" in employees:
    print("Yes, Tammy works here.")



employees = ['Sara', 'Tammy', 'Debbie', 'John', 'Carrie']
if "Dave" in employees:
    print("Yes, Tammy works here.")


print(len(employees))



#Practice

#change items

cars = ['Toyota', 'Ferrari','Porsche','Mercedes', 'Audi']
print(cars)

cars[3] = 'Skoda'
print(cars)

#delete items

cars = ['Toyota', 'Ferrari','Porsche','Mercedes', 'Audi']

del cars[2]

print(cars)

#insert a car

cars.insert(2,'Mitsubishi')
print(cars)


#Code academy while loops

#I am learning about variables in while loops- from code academy
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 

#Variable assigned for the length of python topics
length = len(python_topics)

#variable and initialize as 0 
index = 0 

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1



#Breaking loops in python

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"


for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    break

print("They have the dog I want!")


#continue conditional statement for loops 

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)



#nested loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]


scoops_sold = 0

for location in sales_data:
  for scoops in location:
    scoops_sold += scoops


print(scoops_sold)

#List comprehension

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [scaled + 10 for scaled in grades]
print(scaled_grades)

# this out puts the grades adding 10 points












