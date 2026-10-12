# Password Generator

# Importing random module 
import random

# Importing string module 
import string 

# Creating function 
def password_generator(length):

    # Creating collection
    characters = string.ascii_letters + string.digits + string.punctuation

    # Creating empty list
    password = []

    # Loop for length
    for _ in range(length):
        password.append(random.choice(characters))
    
    # Shuffling password
    random.shuffle(password)

    # Joining characters
    return "".join(password)

# Taking length from user
length = int(input("Enter password length:"))

# Checking using condition
if length >= 8:
    password = password_generator(length)
    print(f"Password: {password} generated successfully!")
else:
    print("Password is invalid!")



