# 0 divide 0 error

try:
    print(0/0)

except ZeroDivisionError:
    print("You can't divide by 0!")


print("-----------------------")

import sys

try:
    num = int(input("Enter a number between 1 - 10: "))
except ValueError:
    print("Please a number input only!")
    sys.exit() #Force exits gracefully after the error

print("You entered the number", num)




    

    
