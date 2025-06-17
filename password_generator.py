import random
import string

# Ask user for how long password 
length = int(input("How many characters do you want in your password? "))

# Characters to use in the password
letters = string.ascii_letters  # A-Z and a-z
numbers = string.digits         # 0-9
symbols = string.punctuation    # Special characters like !@#$%^&*

# Combine everything into one 
all_chars = letters + numbers + symbols

# Generate the password
password = ""
for i in range(length):
    password += random.choice(all_chars)

# Show the password 
print("Here is your password:", password)
