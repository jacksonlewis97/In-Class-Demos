#Use type() to see the data type of an object
my_string = 'Upward Bound'
my_int = 87
my_float = 8.7
my_bool = True

print(type(my_string))
print(type(my_int))
print(type(my_float))
print(type(my_bool))

#Basic Arithmatic operators
num_1 = 72
num_2 = 19

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)

print(num_1 ** num_2)
print(num_1 // num_2)
print(num_1 % num_2)

#Import math module and access functions
import math

print(math.sqrt(200))

#Import random module and access functions to get a random float and randome int
import random as r
r.seed(3743)
my_random = r.random() #Saving a random float to a variable
print(my_random)
print(r.randint(0,2)) #Printing a random int directly to terminal


