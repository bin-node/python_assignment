def JTOI():
    file = open("words.txt","r")
    data = file.read()
    for letter in data:
        if letter == 'j':
            print("i",end="")
        else:
            print(letter,end="")

    file.close()

JTOI()
