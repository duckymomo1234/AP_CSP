# AP, Reading and writing to files

with open("practice.txt", "r+") as file:
    content = file.read()
    content = " Chapter 1:\n" + content + " and Christopher Robin was sitting on his doorstep, putting on his big boots"
    file.write(content)

    with open("practice.txt", "a") as file:
        file.write("\nWinnie the Pooh and the Blustery Day")
       