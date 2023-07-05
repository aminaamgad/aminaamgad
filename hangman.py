import random
from words import words
from hangman_visual import lives_visual_dict
import string


def validword(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = validword(words)
    lettersinword = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    lettersused = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(lettersinword) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(lettersused))

        # what current word is (ie W - R D)
        wordlist = [letter if letter in lettersused else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(wordlist))

        userletter = input('Guess a letter: ').upper()
        if userletter in alphabet - lettersused:
            lettersused.add(userletter)
            if userletter in lettersinword:
                lettersinword.remove(userletter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', userletter, 'is not in the word.')

        elif userletter in lettersused:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died. The word was', word)
    else:
        print('You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
