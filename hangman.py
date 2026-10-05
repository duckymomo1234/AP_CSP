# AP, Hangman

# Create a list of ten words on a seperate text file !
# Create another file hold win/loss counts !
# Read the files

# Use split(",") on the content of the words txt document to create your lost of words !
# Pull win  and lose totals from the other txt file you made save them as two seperate variables
# Build the hangman game
    # Save the correct word as a varible random.choice(name of list)
    # number of guesses
    # What letters have been guessed []
    # Functions to display the hangmas (needs number of wrong guesses)
'''
__________
|        |
|        O
|       /|\\
|       / \\
|
|__________ 
'''


#Function to show teh letters and spaces (The correct word, letters that have been guessed)
  # variable for display word
# loop over the correct word
    # Check if letter has been guessed
        # then add the letter to teh dsplay word
    # if they havent guessed the letter 
        # add an underscore to teh display
#return the finished display word (outside of loop)


# Main game loop (While true)
    # call function to show hangman
    # print function call to show display word
    # create variable and ask user to guess a letter
    # add the lletter to list of guessed layers 
    # check if not letter in word:
        # increase incorrect guesses
# check if display word is same as the word
    # tell user they won
    # increase win total
    # ask if they want to play again
        # reset random word, rest wrong guess count, guessed letters
 # check to see if they lost (if they have 6 wrong guesses)  
    # Tell them they lost
    # tell them what the word was
    # INCREASE the lost count
    # ask if they want to play again

import random

word_contents = ""

with open("hangman.txt", "r") as file:
    word_content = file.read()

word_list = word_contents.split("\n")

random_word_index =  random.randint(0, len(word_list) - 1)
word_to_guess = word_list[random_word_index]

print(word_to_guess)

with open("win&lose_HM.txt", "a") as file:
        file.write("\nscore")
    