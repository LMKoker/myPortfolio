answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it right first try")
else:
    if guess < answer:
        print("Guess Higher")
    else: # guess must be greater than answer
        print("Lower")
    guess = int(input())
    if guess == answer:
        print("You did it")
    else:
        print("You done goofed")
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have failed")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have failed")
# else:
#     print("You got it first time")