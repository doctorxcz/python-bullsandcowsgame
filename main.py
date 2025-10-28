# Import necessary libraries 📚
import random
import time

# def sections for better organization 🧩
def welcome_message():
    """
    Displays the welcome message for the game
    """
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)
    print("Enter a number:")
    print("-" * 47)

# Function to generate a random 4-digit number with unique digits ⚙️
def generate_secret_number():
    """
    Generates a random 4-digit number with unique digits and returns it as a string with random module.

    Returns:
        str: A 4-digit string with unique digits from list of digits.
    """
    digits = list("0123456789")
    random.shuffle(digits)
    # If first digit is 0, swap it with a non-zero digit to ensure the number doesn't start with zero
    if digits[0] == "0":
        # Find first non-zero digit and swap
        for i in range(1, len(digits)):
            if digits[i] != "0":
                digits[0], digits[i] = digits[i], digits[0]
                break
    return "".join(digits[:4])
# Function to calculate bulls and cows using sum and zip functions 🐂🐄
def get_bulls_and_cows(guess, secret):
    """
    Compares the guess with the secret number and returns the count of bulls and cows with sum and zip functions.
    Args:
        guess (str): The guessed 4-digit number as a string.
        secret (str): The secret 4-digit number as a string.
    Returns:
        tuple: A tuple containing the number of bulls and cows.
    
    """
    bulls = sum(g == s for g, s in zip(guess, secret))
    cows = sum(min(guess.count(n), secret.count(n)) for n in set(guess)) - bulls
    return bulls, cows

def duplicate_check(guess):
    """
    Checks if the guess has duplicate digits.
    Args:
        guess (str): The guessed 4-digit

    Returns: bool: True if there are duplicate digits, False otherwise.
    """
    return len(set(guess)) != len(guess)







# Main function to run the Bulls and Cows game 🐂🐄✅

def main():
    # This is the main backbone of the code
    welcome_message()
    secret_number = generate_secret_number()
    attempts = 0
    start_tracking_time = time.time() # Start time tracking
    #print(secret_number)  # For testing purposes, remove or comment out in production
    while True: # Main game loop
        guess = input(">>> ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        if guess[0] == "0":
            print("The first digit cannot be ZERO. Please try again.")
            continue
        if duplicate_check(guess): # Check for duplicate digits with bool True/False function
            print("All digits must be unique. Please try again.")
            continue

        attempts += 1
        bulls, cows = get_bulls_and_cows(guess, secret_number)
        #BUILD cow/cows and bull/bulls grammar for output
        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"
        
        print(f"{bull_word} {bulls}, {cow_word} {cows}")
        print("-" * 47)
        if bulls == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            end_tracking_time = time.time() # End time tracking
            elapsed_time = end_tracking_time - start_tracking_time
            print(f"Time taken: {elapsed_time:.2f} seconds") 
            pokračovat = input("Do you want to play again? (yes/no): ").strip().lower()
            if pokračovat == "yes":
                main()  # Restart the game
            else:
                print("Thank you for playing! Goodbye!")
            break


# Main entry point
if __name__ == "__main__":
    main()








