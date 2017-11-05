# Hangman
# A game by Salvador, Natalia and Teresa
# 11/4/2017

import random

# constants
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
    ===''','''
  +---+
  0   |
      |
      |
    ===''','''
  +---+
  0   |
  |   |
      |
    ===''','''
  +---+
  0   |
 /|   |
      |
    ===''','''
  +---+
  0   |
 /|\  |
      |
    ===''','''
  +---+
  0   |
 /|\  |
 /    |
    ===''','''
  +---+
  0   |
 /|\  |
 / \  |
    ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
    ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
    ===''']

WORDS = '''pizza tacos apple orange pear soup tangerine noodles banana burrito water smoothie
coffee tea fries chips corn spaghetti sushi ramen lettuce soda hamburger milk cheese candy yogurt
pepper cabbage pineapple onion carrot watermelon salt pretzel broccoli peanut fish donut cake
brownie cupcake '''.split()


# ["pizza", tacos", "apple", orange"]
def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


# show drawing and blanks to player
def print_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])  # this is where its wrong. Hangman pics at the index at 7
    print()
    print("Missed letters: ")
    for letter in missed_letters:
        print(letter, end="")
    print()
    blanks = "_" * len(secret_word)
    for i in range(0, len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter + " ", end="")
    print()

def get_guess(already_guessed):
    while True:
        print("Guess a letter:")
        guess = input().lower()
        if len(guess) != 1:
            print("Please guess a single letter at a time.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("That is not a letter. Try again.")
        else:
            return guess

def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def play():
    print("FOODMAN")
    print("A game by Salvador, Natalia and Teresa")
    missed_letters, correct_letters = "", ""
    secret_word = get_random_word(WORDS)
    stop_game = False
    amount_of_games = 0
    amount_of_won = 0
    amount_of_lost = 0
    while not stop_game:
        # show drawing and blanks to player
        print_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters += guess
        else:
            missed_letters += guess
        # check if player has won
        # To do so, you need to compare what they've guessed to the secret word
        # Essentially, check if all the letters in secret_word are in correct_letters
        i = 0
        match = True
        while match and i < len(secret_word):
            if secret_word[i] not in correct_letters:
                match = False
            i += 1
        if match:
            print("Yes! The secret word is " + secret_word + "! You win!")
            amount_of_won += 1
            amount_of_games += 1
            stop_game = True
        elif len(missed_letters) == len(HANGMAN_PICS) - 1: #length of Hangman Pictures = 7, missed = 7; Player loses
            print_board(missed_letters, correct_letters, secret_word)
            print("You have run out of guesses!")
            print("After " + str(len(missed_letters)) + " missed guesses and " + str(len(correct_letters))
                  + " correct guesses, the secret word was " + secret_word)
            amount_of_lost += 1
            amount_of_games += 1
            stop_game = True
        print("You have played", amount_of_games, "games.")
        print("You have won", amount_of_won, "games and have lost", amount_of_lost, "games.")
        print("Points:", amount_of_won - amount_of_lost,)
        if stop_game:
            if play_again():
                missed_letters, correct_letters = "", ""
                stop_game = False
                secret_word = get_random_word(WORDS)
            else:
                print("Goodbye!")

play()
