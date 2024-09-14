import random
# Create a guessing game. 
# The program should pick a random number between 1 and 10, and the user has to guess the number. 
# The program should give feedback if the guess is too high or too low.

computer_pick = random.randint(1, 11)

user_guess = int(input("I guess:"))

if (user_guess < computer_pick):
    print(f"Computer pick: {computer_pick}, you guess lower")
elif (user_guess > computer_pick):
    print(f"Computer pick: {computer_pick}, you guess higher")
else:
    print(f"Computer pick: {computer_pick}, you guess correct")