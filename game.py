import random

print("Guess the Number Game")
print("=====================")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Ask the user to make a guess
guess = int(input("Make a guess: "))

# Keep track of the number of tries
tries = 1

# Keep looping until the user guesses the correct number
while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    tries += 1
    guess = int(input("Make a guess: "))

# The user has guessed the correct number
print("You got it in", tries, "tries!")