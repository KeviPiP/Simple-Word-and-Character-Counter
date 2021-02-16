while True:
    x = input("Type here: ")

    # counts the number of words
    pist = len(x.split())
    # counts the number of characters
    char = len(x)

    print(pist, "words.")
    print(char, "characters.")

    usr_input = input("Continue? Y/N: ")
    inpt = usr_input.lower()

    if inpt == "y":
        continue

    else:
        print("Goodbye...")
        break
