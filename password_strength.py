# AP, password strength assinment

characters = False
uppercase = False
lowercase = False
number = False
symbol = False
password = input("What is your password:")

(len(password))
for letter in password:
    if len(password) >= 8:
        characters = True
else:
    characters= False

if letter.isupper():
    uppercase = True
else:
    uppercase = False

if letter.islower():
        lowercase = True
else:
    lowercase = False