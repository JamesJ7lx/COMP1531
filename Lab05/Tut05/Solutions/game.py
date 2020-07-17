import random

class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def guess(self, previous_guesses):
        print(f"Please make a guess {self.name}")
        print(f"Previous guesses are: {previous_guesses}")
        guess = int(input("Guess? "))
        return guess

class AIPlayer:
    def __init__(self, name):
        self.name = name

    def guess(self, previous_guesses):
        numbers_left = [i for i in range(1, 101) if i not in previous_guesses]
        guess = random.choice(numbers_left)
        return guess

def play_game(players):
    answer = random.randint(1, 100)
    winner = None
    previous_guesses = []
    while winner is None:
        for player in players:
            guess = player.guess(previous_guesses)
            print(f"{player.name} guessed {guess}")
            previous_guesses.append(guess)
            if guess == answer:
                winner = player
                break
    print(f"Congratulations {winner.name}, you won!")

# Testing it out
play_game([HumanPlayer("Rob"), HumanPlayer("Isaac"), AIPlayer("Marvin")])
