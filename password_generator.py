import random
import string

length= int(input("Enter password length (minimum 4):"))

if length<4:
    print("Password length must be at least 4.")
else:
    characters =string.ascii_letters + string.digits + string.punctuation
    password= "".join(random.choice (characters) for _ in range(length))
    print("Generated password:",password) 