# Your code below:
#Pizza Toppings 
toppings = ["pepperoni", "pinapple", "cheese", "sausage", "olives", "anchiovies", "mushrooms"]

print(toppings)
print("---------------------------------------------------------------")

#Prices
price = [2, 6, 1, 3, 2, 7, 2]

#Number of slices costing £2
num_two_dollar_slices = price.count(2)

print(num_two_dollar_slices)

#number of pizzas
num_pizzas = len(toppings)

print(num_pizzas)

print("---------------------------------------------------------------")

#print string we sell and x pizzas

print("We sell " + str(num_pizzas) + " different kinds of pizza")

print("---------------------------------------------------------------")

#combine pizza price and name 

pizza_and_price = [2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchiovies"], [2, "mushrooms"]

print(pizza_and_price)

print("---------------------------------------------------------------")

#sort by ascending price

pizza_and_price = sorted(pizza_and_price)

print(sorted(pizza_and_price))

print("---------------------------------------------------------------")

# store first element in cheapest pizza var

cheapest_pizza = pizza_and_price[0]

print(cheapest_pizza)

print("---------------------------------------------------------------")

#guy orders most expensive on menu 
most_expensive = pizza_and_price[-1]
print(most_expensive)

print("---------------------------------------------------------------")

#we ran out of anchiovies - remove it from pizza and prices
#.pop alone removes last item in list 

pizza_and_price.pop()
print(pizza_and_price)

print("---------------------------------------------------------------")

#add new peppers topping to original list at correct assending price index point 

pizza_and_price.insert(4, [2.5, "peppers"])
#                    (index point [variable item, variable item])

print(pizza_and_price)

print("---------------------------------------------------------------")

#store cheapest pizzas in three cheapest variable

three_cheapest = pizza_and_price[0:3]
print(three_cheapest)

