weight = 0.5

#Ground Shipping 

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20 
else:
  cost_ground = weight * 4.75 + 20 

print("The price of Ground Shipping is: " + "£" + str(cost_ground))


# Ground Premium 
cost_ground_premium = 125.00

print("The price of Premium Ground Shipping is: " + "£" + str(cost_ground_premium))


#Drone shipping 

if weight <= 2:
  cost_drone = weight * 4.5 
elif weight <= 6:
  cost_drone  = weight * 9.00 
elif weight <= 10:
  cost_drone = weight * 12.00 
else:
  cost_drone = weight * 14.25 

print("The price of Drone Shipping is: " + "£" + str(cost_drone))

# Printing the cheapest method
if cost_ground < cost_ground_premium and cost_ground < cost_drone:
  print("Ground Shipping is the cheapest method!")
elif cost_ground_premium < cost_drone:
  print("Ground Shipping Premium is the cheapest method!")
else:
  print("Drone Shipping is the cheapest method!")
