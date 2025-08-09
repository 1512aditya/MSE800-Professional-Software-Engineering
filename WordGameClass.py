import random

words = ("python", "random", "easy", "MSE800")
class WordGame:
    def __init__(self):
        self.correct = random.choice(words)
        self.attempt = 3
    
        print("""
        Welcome to WORD Game!!!
        (Press Enter without typing anything to quit)
        """)
    
        print("The guess the word from list you got only 3 lives:", words)
    
        while self.attempt > 0:
            guess = input("Your guess: ")
            if guess == "":
                break
            elif guess == self.correct:
                print("That's it, you guessed it!\n")
                break
        else:
            self.attempt -= 1
            if self.attempt > 0:
                print("Sorry, that's not it.")
            else:
                print(f"Out of guesses! The correct word was '{self.correct}'.")
    
    

    
        print("Thanks for playing!")



if __name__ == "__main__":
    WordGame()
