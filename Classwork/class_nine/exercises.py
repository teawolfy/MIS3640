#EXERCISE 1.1
word = open('words.txt')
line = repr(fin.readline())

def read_long_words(wordList):
    """
    prints only the words with more than 20 characters
    """
    wordCount = 0
    lineCount = 0
    for word in wordList:
        if len(word) > 20:
            print word
            wordCount += 1
        lineCount += 1
    pass
    
read_long_words(word)

#EXERCISE 1.2
def has_no_e():
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    wordCount = 0
    lineCount = 0
    for line in word:
            if line.find('e') == -1:
                print line
                wordCount += 1
            lineCount += 1
words(word)

#EXERCISE 1.3
def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    pass

#EXERCISE 1.4
def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True

print(uses_only('Babson','aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))

#EXERCISES 1.4
def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for word in required:
        if letter not in word:
            return False
    return True

print(uses_only('Babson','abs'))
print(uses_only('college', 'abs'))

#EXERCISE 1.5
def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0]
    for letter in word:
        if letter < before:
            return False
    return True