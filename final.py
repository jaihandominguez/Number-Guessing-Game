import random

class NumberGuessingGame:
    def __init__(self, low = 1, high = 100):
        self.low = low
        self.high = high
        self.target_number = random.randint(self.low, self.high)
        self.attempts = 0
        self.guess_history = []
    
    def get_valid_guess(self):
        # Prompts the user for input and validates it
        # Ensures input is an integer within the range
        while True:
            user_input = input(f"Enter a number between {self.low} and {self.high}: ")
            try:
                guess = int(user_input)
                if guess < self.low or guess > self.high:
                    print(f"Please enter a number between {self.low}-{self.high}: ")
                    continue
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def check_guess(self, guess):
        # Compares guess with target number and gives feedback
        if guess > self.target_number:
            print("Too high! Try a lower number.")
        elif guess < self.target_number:
            print("Too low! Try a higher number")
        else:
            print("Congratulations! You guessed the correct number!")
            return True
        return False

    def play(self):
        # Main game loop
        print("\nWelcome to the Number Guessing Game")
        print(f"I have selected a number between {self.low} and {self.high}.")
        print("Try to guess it!\n")
        while True:
            guess = self.get_valid_guess()
            self.attempts += 1
            self.guess_history.append(guess)
            if self.check_guess(guess):
                break
        self.display_summary()

    def display_summary(self):
        # Displays game results
        print("\nGame Summary:")
        print(f"Total attempts: {self.attempts}")
        print(f"Your guesses: {self.guess_history}")

def main():
    #Entry point of the game
    game = NumberGuessingGame()
    game.play()

if __name__ == "__main__":
    main()