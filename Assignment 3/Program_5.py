import re

password = input("Enter a password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[@#$%&*]", password)):
    print("Strong Password")
else:
    print("Weak Password")
