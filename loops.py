# AP, Loops Notes 
import random

count = 1

while count <= 10:
    print(count)
    count += 1

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("Duck....")
    ducks += 1 #ducks = ducks + 1
print("GOOSE!!!!")

# Complex data type = hold other data in it
siblings = ["Ian", "Quintin", "Violet", "Ashton"]
print(siblings[2])
#adding to a list
siblings.append("Lena")      #adds to the end of a list
siblings.insert(2, "Alice")          
print(siblings)
#Remove from a list
siblings.pop()       # <= if no number given pop removes the last item

#print each item in a list
for sibling in siblings:
    print(sibling)

# For Loops
for num in range(1,25):
    if num % 15 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)