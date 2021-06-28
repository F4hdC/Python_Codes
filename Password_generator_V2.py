# F4hdC ©
#Password Generator ~ Other Method

import string
import random

# Get the input 
size = int(input("Size of password? [min 8]:  "))

if (size < 8):
    print("The minimum is 8 Characters")
    quit()

letters_upp = string.ascii_uppercase
letters_low = string.ascii_lowercase
symbols     = "!$%&/()=?;{^*}+-_^[:]"
numbers     = "01234566789"

password    = []
rest        = 0
pass_rand   = ''

# The idea is, if the input can be parted in 4 parts, Good
# Otherwise i add 1 to the size until it's divisible by 4, and i put it in the size_aux
# And Finally choose randomly just the length of the size as it was inserted by the user from the size_aux's String
# The number 4 is because there are 4 types of characters

"""def divisible_by_4(size):
    if(size%4==0):
        return size
    else:
        return divisible_by_4(size+1)
"""
# the best way to find the divisible by 4 is here
def divisible_best_way(size):
    if(size%4==0):
        return size
    else:
        return size+(size%4)

size_aux = divisible_best_way(size) # Here, i Know that size_aux is divisible by 4
parts = int(size_aux/4)

for i in range(parts):
    password.append(random.choice(letters_low))
    password.append(random.choice(letters_upp))
    password.append(random.choice(symbols))
    password.append(random.choice(numbers))

pass_rand = ''.join(random.sample(password,size)) # To convert the list to String

print("The Password Generated is : "+pass_rand) # Finally Print the result
#print(len(pass_rand))