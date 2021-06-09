# F4hdC ©
#Password Generator ~ Hard

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

if (size%2)==0:
    parts = int(size / 4)  
else:
    parts = int((size-1)/4)

for i in range(parts):
    password.append(random.choice(letters_low))
    password.append(random.choice(letters_upp))
    password.append(random.choice(symbols))
    password.append(random.choice(numbers))

if(int(len(password))==size):
    {}
else:
    rest = size - len(password)

if (rest == 1):
    password.append(random.choice(symbols))
elif(rest == 2):
    password.append(random.choice(symbols))
    password.append(random.choice(letters_upp))
elif(rest == 3):
    password.append(random.choice(symbols))
    password.append(random.choice(letters_upp))
    password.append(random.choice(symbols))

pass_rand = ''.join([str((i)) for i in password])

print("Password_ Hard : ",''.join(random.sample(pass_rand,size)))
