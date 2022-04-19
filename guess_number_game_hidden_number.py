# import random module 
import random

# set varaible to a random number
num=random.randint(0,100)

r = -1

while r != num:
    #print the variable "r"
    r = int(input("Type your number here: "))
    
    
    # If r is guessed correctly print equal 
    if r == num:
        print("equal")
    
    # If variavle "r" is greater than varial "num" print Higher 
    elif r > num:
        print("Lower")
    
    # If variable "r" is less than variable "num" print Lower 
    elif r < num:
        print("Higher")
