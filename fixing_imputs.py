# AP, Fixing user imputs

while True:
    color = input("Tell me a color that is only one word:").strip().lower()
        if color.isnumeric():
            print("That is a number not a number!")
    elif " " in color:
        print"("I said one word")
    else:
        break

print(f"We painted the walls {color}!")