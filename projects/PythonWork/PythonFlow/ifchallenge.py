name = input("What is your name? ")
age = int(input("Alright now how old are you? "))

if 18 <= age <= 30:
    print("Welcome to our Premium Holiday {}".format(name))
else:
    print("I'm sorry {}, but you are not eligible for this holiday".format(name))