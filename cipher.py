# AP, cipheR

#ENCRYPTING

# Looking at sugested outputs
# Start without finctions
# Start with letter 1 and all 3 variables
# Build a working loop tha twill pring out you ruser
#build a conditional inside pf a loop tp see of specific leter is a characte, and if it convert to number, increase by whatever number your user gave you, convert it back to letter, print it 
# Needs to have a variable where O save all bariables as i change or dont change the ONLY LETTERS
# If pass end of the alphabet check before coverting it back to character do SUBTRACTION to take us back to the begining  of the alphbet

#DYCRYPTING

# Number given by user HAS TO BE A NEGITIVE

#    number += 2
#    print(f"The letter {lower_start} is the number {ord(lower_start)}")
#    print(f"The letter {chr(number)} is the number {number}")
#    print(f"The letter {lower_end} is the number {ord(lower_end)}")

suggested_output = input("Would you like to (E)ncrypt or (D)crypt a message?:")
message = input("What is your message?:")
shift = input("How many times would you like to shift?:")

for letter in message:
    if letter.isalpha():
        letter = ord(letter)
        letter = 

    