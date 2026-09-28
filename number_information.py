# AP, number information assignment

for number in range(1,21):
    if number % 15 == 0:
        print('FizzBuzz')
    elif number % 2 == 0:
        print(number "is even")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)