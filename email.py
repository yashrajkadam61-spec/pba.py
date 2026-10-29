#write a python script using regular expression to validate email addreses entered by the user.
import re

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email = input("Enter your email address: ")

if re.fullmatch(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")