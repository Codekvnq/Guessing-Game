from colors import *
from random import randint

# Welcome Screen Msg
print(BLUE, '**** Welcome To Your World Of Guessing ****')
user_input = int(input(WHITE + 'Choose Your Level\n'
                               '1. Normal (1 - 50)\n'
                               '2. Intermediate (1 - 200)\n'
                               '3. Hard (1 - 500)\n'
                               '4. Exit Application\n\n'
                               'Enter Request : '))
# user's option
if user_input == 1:
    guess_range = 50
elif user_input == 2:
    guess_range = 200
elif user_input == 3:
    guess_range = 500
elif user_input == 4:
    print('**** Thanks For Using Our App, Hope To See You Again!!! **** ')
    exit(1)
else:
    print(RED, 'INVALID REQUEST, TRY AGAIN !!!')

# Generate random number between certain range
generate_number = randint(1, guess_range)

# user chances
user_chances = 4

# accepting the user input and validating, if it matches generated numbers
for i in range(4):
    user_guesses = int(input(WHITE + 'Provide Your Guess Number : '))

    # Determine if the guess is correct
    if user_guesses == generate_number:
        print(GREEN, f'Hurray!!!, You Guessed It Correct.')
    elif user_guesses > generate_number:
        print(YELLOW, f'Your Guess Is To High, Try Again! ')
    elif user_guesses < generate_number:
        print(YELLOW, 'Your Guess Is Too Low, Try Again! ')
    # reduce the user chances and prompt user chances left
    user_chances -= 1
    print(f'Number Of Chances Left is: {user_chances}')

# inform user of the correct guess number
if user_chances == 0:
    print(RED, f'Sorry The Correct Guess Is : {generate_number}')
