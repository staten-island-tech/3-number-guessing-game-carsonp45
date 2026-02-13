import random
random_number = random.randint(1,10)
Number = ""

while Number != random_number:
    try: 
Number_input = input("Guess the correct number? (type random number from 1-10 to finish):")
Number = int(guess_input)
if Number == random_number:
    print("Correct!")
else:
    print("Wrong! Try again.")
