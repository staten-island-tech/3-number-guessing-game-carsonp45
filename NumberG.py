""" import random
random_number = random.randint(1,10)
print("Random number", random_number)
count = 1

while count > 0:
    print("Wrong", count)
    count = count + 1

number = "random"
while number != "correct":
    order = input("Guess the number)   (type 'random_number'to finish):")
print("Correct!") """


import random

# Generate a random number between 1 and 10 (inclusive)
random_number = random.randint(1, 10)
print("A random number between 1 and 10 has been generated.")

# Initialize the user's guess variable to something that isn't the correct number
guess = None
# Initialize the guess count
count = 0

# Loop until the user's guess matches the random number
while guess != random_number:
    try:
        # Get user input and convert it to an integer
        guess_input = input("Guess the number (or type 'quit' to exit): ")

        if guess_input.lower() == 'quit':
            print(f"The correct number was {random_number}. Exiting game.")
            break

        guess = int(guess_input)
        count += 1

        if guess < random_number:
            print(f"Too low! Try again.")
        elif guess > random_number:
            print(f"Too high! Try again.")
        else:
            # This block is executed if the guess is correct
            print(f"Correct! You guessed the number in {count} attempts.")

    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Invalid input. Please enter a whole number or 'quit'.")