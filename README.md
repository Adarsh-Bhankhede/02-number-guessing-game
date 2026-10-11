
# 🎯 Number Guessing Game

**Week 2 - Project 2**

## Description

Write a Python program in which the computer randomly selects a number within a specified range, and the player tries to guess it.

The program provides hints to help the player by indicating whether the guessed number is too high or too low. The game continues until the player guesses the correct number or runs out of attempts.

## Features

- Generate a random number within user-defined limits.
- Allow the player to guess the number.
- Display hints when the guess is too high or too low.
- Limit the number of attempts to 10.
- Display the correct number if the player runs out of attempts.
- Allow the player to play again.
- Track and display successful guessing attempts from previous rounds.
- Handle invalid numerical input.

## Program Flow

1. Display the welcome message.
2. Ask the user to enter the lower and upper limits.
3. Generate a random number within the specified range.
4. Allow the user to guess the number, with a maximum of 10 attempts.
5. If the guess is correct:
   - Display a congratulatory message.
   - Record the number and attempts taken.
6. If the guess is too high or too low:
   - Display an appropriate hint.
   - Allow the user to try again.
7. If the player runs out of attempts, display the correct number.
8. Ask the user whether they want to play again.
9. When the user exits, display the successful guessing attempts.

## Concepts Used

- `random` module
- `random.randint()`
- `while` loops
- `if-elif-else` statements
- `try-except` for error handling
- User input and type conversion
- Lists and list methods
- `sorted()` function
- `lambda` function
- F-strings
