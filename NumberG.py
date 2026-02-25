import random
random_number = random.randint(1,10)
guess = None
guesses = []
while guess != random_number:
    Number_input = input("Guess the correct number? (type random number from 1-10 to finish):")
    guess = int(Number_input)
    guesses.append[guess]
    guess += 1
    if guess == random_number:
        print("Correct!")
        print("These were all the guesses you made", guesses)
    else:
        print("Wrong! Try again.")
    if guess > random_number:
        print ("Lower")
        print("These were all the guesses you made", guesses)
    if guess < random_number:
        print ("Higher")
        print("These were all the guesses you made", guesses)