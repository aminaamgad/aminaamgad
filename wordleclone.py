import random

def generate():
    
    words = ['apple', 'pear', 'peach', 'grape', 'orange', 'banana', 'melon', 'lemon', 'cherry']
    return random.choice(words)

def play():
    
    word = generate()
    print("Welcome to Wordle!")
    print("The word has 5 letters.")
    guess = ""
    attempts = 0
    while guess != word:
        guess = input("Enter your guess: ")
        if len(guess) != 5:
            print("Invalid guess! The word has 5 letters.")
        else:
            result = ""
            for i in range(len(word)):
                if guess[i] == word[i]:
                    result += guess[i].upper()
                elif guess[i] in word:
                    result += guess[i].lower()
                else:
                    result += "-"
            print(result)
            attempts += 1
            if guess == word:
                print("You guessed the word in", attempts, "attempts!")
            else:
                print("Wrong. The word was {word}")
    
play()
