import random
import os

class GamePack:
    def __init__(self):
        self.score = 0
        self.words = ["python", "coding", "computer", "keyboard", "laptop", "program"]
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def number_guessing(self):
        print("\n=== NUMBER GUESSING (1-100) ===")
        secret = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"Guess {attempts+1}/{max_attempts}: "))
                attempts += 1
                
                if guess == secret:
                    print(f"🎉 Correct! Took {attempts} attempts.")
                    self.score += (8 - attempts) * 10
                    return
                elif guess < secret:
                    print("Too low!")
                else:
                    print("Too high!")
                    
            except ValueError:
                print("Enter a number!")
        
        print(f"Game over! It was {secret}")
    
    def hangman(self):
        print("\n=== HANGMAN ===")
        word = random.choice(self.words).upper()
        guessed = set()
        wrong = 0
        max_wrong = 6
        
        while wrong < max_wrong:
            display = ''.join([c if c in guessed else '_' for c in word])
            print(f"\nWord: {display}  Wrong: {wrong}/{max_wrong}")
            
            if set(word) <= guessed:
                print("🎉 You won!")
                self.score += 50
                return
            
            guess = input("Guess a letter: ").upper().strip()
            if len(guess) != 1 or not guess.isalpha():
                print("One letter only!")
                continue
            
            if guess in guessed:
                print("Already guessed!")
                continue
            
            guessed.add(guess)
            if guess not in word:
                wrong += 1
                print("Wrong!")
        
        print(f"Game over! Word was: {word}")
    
    def rock_paper_scissors(self):
        print("\n=== ROCK PAPER SCISSORS (Best of 3) ===")
        choices = ["rock", "paper", "scissors"]
        wins = 0
        
        for round_num in range(3):
            print(f"\nRound {round_num+1}/3")
            player = input("rock/paper/scissors: ").lower().strip()
            if player not in choices:
                print("Invalid!")
                continue
            
            computer = random.choice(choices)
            print(f"Computer: {computer}")
            
            if player == computer:
                print("Tie!")
            elif (player == "rock" and computer == "scissors") or \
                 (player == "paper" and computer == "rock") or \
                 (player == "scissors" and computer == "paper"):
                print("You win round!")
                wins += 1
            else:
                print("Computer wins round!")
        
        if wins >= 2:
            print("🎉 You won the match!")
            self.score += 30
        else:
            print("Match lost!")
    
    def show_menu(self):
        self.clear_screen()
        print("=== GAME PACK ===")
        print(f"Score: {self.score}")
        print("1. Number Guessing")
        print("2. Hangman")
        print("3. Rock Paper Scissors")
        print("4. Quit")
        
        choice = input("\nChoose (1-4): ").strip()
        return choice

def main():
    games = GamePack()
    
    while True:
        choice = games.show_menu()
        
        if choice == "1":
            games.number_guessing()
            input("\nPress Enter to continue...")
        elif choice == "2":
            games.hangman()
            input("\nPress Enter to continue...")
        elif choice == "3":
            games.rock_paper_scissors()
            input("\nPress Enter to continue...")
        elif choice == "4":
            print(f"\nFinal score: {games.score} 🎮")
            break
        else:
            print("Invalid choice!")
            input("Press Enter...")

if __name__ == "__main__":
    main()
