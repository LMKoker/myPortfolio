# Import the modules
import sys
import random

ans = True

while ans:
    question =input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1, 8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("Yes, without a doubt")

    elif answers == 2:
        print("Most likely probably")

    elif answers == 3:
        print("Uh huh")

    elif answers == 4:
        print("Mmmmm not sure ask me again later")

    elif answers == 5:
        print("You're unfocused. Try again")

    elif answers == 6:
        print("¯\_(ツ)_/¯")

    elif answers == 7:
        print("Naaaaaaah")

    elif answers == 8:
        print("Nope noooooooooope")