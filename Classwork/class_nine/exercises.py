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
    for line in word:
            if line.find('e') == -1:
                print line
words(word)

#EXERCISE 1.3
def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in word:
        if letter not in forbidden:
            return True
        return False
print(avoids('Babson','aBbsonxyz'))
print(avoids('college','aBbsonxyz'))

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

#EXERCISE 2.1
"""
For is_abecedarian we have to compare adjacent letters, which is a little tricky with a for loop. Use recursion!
"""
def is_abecedarian(word):
    if len(word) <= 1:
        return True
        #If the legth of the word is less than one, there is no adjacent letter to compare to
    if word[0] > word[1]:
        return False
        #if the value of the first letter is greater than the value of the next letter, the function stops
    return is_abecedarian(word[1:]) 

print(is_abecedarian('o'))
print(is_abecedarian('ok'))
print(is_abecedarian('ko'))
        

#EXERCISE 2.2
"""
Rewrite is_abecedarian with a while loop
"""
def is_abecedarian(word):
    c = 0
    while c < len(word)-1:
        if word[c+1] < word[c]:
            return False
        c = c+1
    return True

#EXERCISE 3
def is_triple_double(word):
"""
Returns "True"" if the word contains three consecutive, double letters
"""
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print word