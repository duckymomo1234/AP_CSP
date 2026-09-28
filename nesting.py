# AP, nesting notes

siblings = ["Ian", "Quintin", "Alice", "Violet", "Ashton"]
count = 1
if len(siblings) > 0:
    while count <= len(siblings):
         print(f"{count}. {siblings[count-1]}")
    count += 1
else:
        print("There are no siblings")
