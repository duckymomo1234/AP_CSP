# AP, password strength assinment

characters = False
uppercase = False
lowercase = False
number = False
symbol = False
password_strength = False
password = input("What is your password:")

(len(password))
for letter in password:
    if len(password) >= 8:
        characters = True
    if len(password) < 8:
        characters= False

    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isdigit():
        number = True
    if letter in "!@#$%^&*()":
        symbol = True

score = characters + uppercase + lowercase + number + symbol

if score == 5:
    print("Your password is strong")
elif score >= 3:
    print("Your password is medium")
else:
    print("Your password is weak")

if password_strength == "Strong":
    print("Good job, your password is strong")
else:
    if len == False:
        print("Make your password at least 8 characters long")
    if uppercase == False:
        print("Make your password have at least 1 uppercase letter")
    if lowercase == False:
        print("Make your password have at least 1 lowercase")
    if number == False:
        print("Make your password have at least 1 number")
    if symbol == False:
        print("Make your password have at least 1 symbol")
    