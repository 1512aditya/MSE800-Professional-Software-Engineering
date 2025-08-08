import random

def RandomWords():
    words = ("python", "random", "easy", "MSE800")
    correct = random.choice(words)
    attempt = 3
    
    
    print("""
    Welcome to WORD Game!!!
    (Press Enter without typing anything to quit)
    """)
    
    print("The guess the word from list you got only 3 lives:", words)
    
    while attempt > 0:
        guess = input("Your guess: ")
        if guess == "":
            break
        elif guess == correct:
            print("That's it, you guessed it!\n")
            break
        else:
            attempt -= 1
            if attempt > 0:
                print("Sorry, that's not it.")
            else:
                print(f"Out of guesses! The correct word was '{correct}'.")
    
    
    print("Thanks for playing!")

if __name__ == "__main__":
    RandomWords()
