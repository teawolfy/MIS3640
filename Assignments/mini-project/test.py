# establish how to select random word
import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# will admit, google told me to work the logic this way -> define win state and then the function. I originally was going to define it in the function.
# establishes how the user wins the game


def win_state(guessed_letters, secret_word):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_hangman(secret_word):
    """
    Computer enters into a game of hangman with the user. The computer will select a random word from a list of words, 
    and the user will try to guess the word by inputting one letter at a time. If the user guesses the word correctly
    before the number of turns reaches 0, then they win the game
    """
    print(secret_word)
    print('Get ready to play Hangman!')
    print('I am thinking of a word that is %d letters long' % (len(secret_word)))
    number_of_guesses = 8
    available_letters = []
    for i in range(97, 123):
        available_letters.append(chr(i))
    guessed_letters = []
    while number_of_guesses > 0 and win_state(guessed_letters, secret_word) == False:
        print('The letters you can guess are: ')
        print(available_letters)
        revealed = ''
        player_guess = ''
        while player_guess not in available_letters:
            # DEBUG CONFUSION: letter guesses must be guessed with '' around -
            # not sure why....
            player_guess = input('Please guess a letter: ')
            # establishing that the guess had to be lowercase
            player_guess = player_guess.lower()
        guessed_letters.append(player_guess)
        available_letters.remove(player_guess)
        for letter in secret_word:
            if letter in guessed_letters:
                revealed += letter
            else:
                revealed += '_'
        if player_guess in secret_word:

            print('That letter was a good guess. %s is in the secret word' %
                  (revealed))
        else:
            number_of_guesses -= 1
            print('Wrong! That letter is not in my word: %s' % (revealed))
        print('You have %d guesses left' % (number_of_guesses))
        print('-------------------------------------------')
    if number_of_guesses == 0:
        print('You lose! The word is %s' % (secret_word))
    else:
        print('You win! The word is %s' % (secret_word))


play_hangman(chooseWord(loadWords()))