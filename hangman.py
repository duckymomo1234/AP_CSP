# AP, Hangman 


import random

with open("hangman.txt", "r") as file:
    words = file.read().split("\n")

try:
    with open("stats.txt", "r") as file:
        stats = file.read().split("\n")
        wins = int(stats[0])
        losses = int(stats[1])
except:
    wins = 0
    losses = 0

word = random.choice(words).lower()
guessed = []
wrong = 0

while wrong < 6:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Guessed letters:", guessed)
    print("Wrong guesses:", wrong)

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong!")
        wrong += 1

    if "_" not in display:
        print("You won! The word was", word)
        wins += 1
        break

if wrong == 6:
    print("You lost! The word was", word)
    losses += 1

with open("stats.txt", "w") as file:
    file.write(str(wins) + "\n")
    file.write(str(losses))

print("Wins:", wins)
print("Losses:", losses)