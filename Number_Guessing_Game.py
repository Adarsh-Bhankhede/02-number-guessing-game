
#? Number Guessing Game

#! program flow 
"""
1. Generate the random number
2. loop
    3. ask user to guess the number
    4. if number == guess
            print congratulations! you guess correct number.
    5. elif number < guess
            print too low
    6. elif number > guess
            print too high
    7. else
            print error: enter valid number

""" 

#! program code:

import random

print("\n=== Welcome To Number Guessing Game ===\n")
all_win_attempts = []
while True:
    print("Choose The Limits for Number To Guess...")
    try:
        lower_limit = int(input("Enter the lower limit of Number: "))
        upper_limit = int(input("Enter the Upper limit of Number: "))
        if lower_limit > upper_limit:
            raise ValueError
    except ValueError:
        print("Please Enter Valid limits.")
        continue 
    
    number_to_guess = random.randint(lower_limit, upper_limit)
    attempts = 1
    while True:
        try:
            guess = int(input(f"Guess the Number ( between {lower_limit} and {upper_limit} ): "))
        except ValueError:
            print('Please enter valid numbers.')
            continue
        if number_to_guess < guess:
            print(f"Too High! Try again {10-attempts} Attempts left.")
            attempts+=1

        elif number_to_guess > guess:
            print(f"Too Low! Try again {10-attempts} Attempts left.")
            attempts+=1
        else:
            print(f"\nCongratulations! You guessed the correct number in  Attempt {attempts}.")
            all_win_attempts.append([number_to_guess, attempts])
            break
        if attempts == 10:
            print("\nYou Lost! Your all attempts Over.")
            print("\nCorrect Number is ",number_to_guess)
            break
   
    choice = input("\nDo you Want to play it again?(Enter y to play again, any char to Exit): ").strip().lower()
    if choice == 'y':
        continue
    else:
        print("\nThank You For Playing....\n")
        break

best_attempts = sorted(all_win_attempts, key=lambda item: item[1])
print("All Best Attempts are: ")
for number, attempt in best_attempts:
    print(f"The Number {number} is guessed in Attempt {attempt}")
    


