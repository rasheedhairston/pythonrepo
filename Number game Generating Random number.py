# import random module 
import random

# set varaible to a static number
num=49

# set variable "r" to populate a random number between 1-100
r = random.randint(0,100)

#print the variable "r"
print(r)

# If r is guessed correctly print equal 
if r == num:
    print("equal")

# If variavle "r" is greater than varial "num" print Higher 
elif r > num:
    print("Higher")

# If variable "r" is less than variable "num" print Lower 
elif r < num:
    print("Lower")
