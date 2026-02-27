import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 0 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_num= random.randint(0,100)

def easy():

    attempt =10
    for num in range(1,11):
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt -= 1  
        if guess == random_num:
            print(f"You got it the answer was {random_num}")
            break
        
        if attempt ==0:
            print("You have run out of guesses.Refresh the page to run again." )
            break

        elif guess > random_num:
            print("Too High. \nGuess again.")

        elif guess < random_num:
            print("Too Low. \nGuess again.")
        
        if attempt ==0:
            print("You have run out of guesses.Refresh the page to run again." )

    

def hard():

    attempt = 5
    for num in range(1,6):
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt -= 1 

        if guess == random_num:
            print(f"You got it the answer was {random_num}")
            break

        if attempt ==0:
            print("You have run out of guesses.Refresh the page to run again." )
            break

        elif guess > random_num:
            print("Too High. \nGuess again.")

        else:
            print("Too Low. \nGuess again.")


if choice == "easy":
    easy()
else:
    hard()