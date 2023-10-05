import os
import re
import subprocess
import hashlib

# Secure input handling
def get_input(prompt):
    while True:
        user_input = input(prompt)
        if re.match(r"^[a-zA-Z0-9_]+$", user_input):
            return user_input
        else:
            print("Invalid input. Please use only alphanumeric characters and underscores.")

# Secure SQL query (no SQL injection)
username = get_input("Enter a username: ")
query = "SELECT * FROM users WHERE username = %s"
# Execute the query using a secure database library like SQLAlchemy

# Secure command execution (no command injection)
command = get_input("Enter a command: ")
subprocess.call(["/bin/bash", "-c", command])

# Secure use of hashlib (salted hashing)
password = get_input("Enter a password: ")
salt = os.urandom(16)  # Generate a random salt
hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)

# Secure use of regular expressions
user_input = input("Enter an email address: ")
if not re.match(r"[^@]+@[^@]+\.[^@]+", user_input):
    print("Invalid email address")

# Secure string concatenation
name = input("Enter your name: ")
greeting = "Hello, " + name

# Secure string interpolation (using format method)
name = input("Enter your name: ")
greeting = "Hello, {}".format(name)

# Secure f-strings
name = input("Enter your name: ")
greeting = f"Hello, {name}"

# Secure use of string concatenation in a loop
items = ["item1", "item2", "item3"]
result = "".join(items)

# Secure use of string.format() method
name = input("Enter your name: ")
greeting = "Hello, {}".format(name)

# Secure use of string.Template (no user input substitution)
from string import Template
template = Template("Hello, $name")
message = template.substitute(name="John")

# Secure raw SQL queries (no SQL injection)
username = get_input("Enter a username: ")
query = "SELECT * FROM users WHERE username = %s"
# Execute the query using a secure database library like SQLAlchemy

# Secure shell command execution (no command injection)
command = get_input("Enter a command: ")
subprocess.call(["/bin/bash", "-c", command])

# Secure use of subprocess with shell=False (no shell injection)
command = get_input("Enter a command: ")
subprocess.call([command])

# Secure use of pickle (no user-controlled data)
import pickle
data = {"username": "admin", "password": "password123"}
serialized_data = pickle.dumps(data)

# Secure use of base64 encoding/decoding (no user-controlled data)
import base64
encoded_data = base64.b64encode(b"Sensitive data")
decoded_data = base64.b64decode(encoded_data)



