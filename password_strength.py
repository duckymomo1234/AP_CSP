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
