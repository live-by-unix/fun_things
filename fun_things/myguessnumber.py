import random

def get_valid_guess():

    while True:
        try:
            user_input = input("Enter your guess: ")
            return int(user_input)
        except ValueError:
            print(" Invalid input you hacker ! Please enter a whole number. Python caught you for sure")

def play_round():
    
    print("\nSelect Difficulty: (1) Easy - 10 tries | (2) Medium - 7 tries | (3) Hard - 3 tries")
    choice = input("Pick a number for ur computer (1-3): ")
    
    if choice == "1":
        limit = 10
    elif choice == "3":
        limit = 3
    else:
        limit = 7 
    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"Game started to save ur computer! You have {limit} attempts.")

    while attempts < limit:
        guess = get_valid_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f" Winner! You got it in {attempts} tries.")
            return True 

    print(f" Out of tries! The number was {secret_number}.")
    return False


print("WELCOME TO THE ULTIMATE NUMBER GUESSING GAME TO SAVE YOUR COMPUTER. GUESS A NUMBER")
while True:
    play_round()
    
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! Goodbye.")
        break