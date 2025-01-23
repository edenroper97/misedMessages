players = ['bob', 'steve', 'michael', 'tom', 'eli', 'bill', 'eden']

print("Here are the first three players on my team:")
for player in players[:3]: #this prints the first 3 people
    print(player.title())

print("---------------------------------------------------")

print("Here are the first three players on my team:")
for player in players[2:5]: #2 to 5... 5 NOT INCLUDED!!!
    print(player.title())

print("---------------------------------------------------")

#slicing increments

nums = [1,2,3,4,5,6,7,8,9]
print(nums[1:8:2])

print("---------------------------------------------------")

#practice time

#8 items - omit first 2, display next 3
cars = ['Toyota', 'Ferrari', 'Kia', 'Seat', 'Renault', 'Audi', 'Mercedes', 'McClaren']
print(cars[2:5])

#8 items, display odd ones

cars = ['Toyota', 'Ferrari', 'Kia', 'Seat', 'Renault', 'Audi', 'Mercedes', 'McClaren']
print(cars[0:8:2])


    
