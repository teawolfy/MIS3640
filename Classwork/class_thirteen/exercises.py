import sys
import string


def process_file(file):
    '''
    Tokenizes a set of text into each word, removing punctuation and making lowercase. 
    Returns an array with all instances of words
    '''
    file = open(file)
    modifiedWords = []
    for line in file.readlines():
        cleanedLine = line.strip()
        words = cleanedLine.split()
        for word in words:
            word = word.translate(string.maketrans("",""), string.punctuation).lower()
            modifiedWords = modifiedWords + [word]
    return modifiedWords


def process_filePG(file):
    '''
    Goes to the beginning of a Project Gutenberg book and tokenizes text into words, removing punctuation and making lowercase. 
    Returns a list of 'word,value' pairs for each instance of a token output to the file 'output.txt'. 
    Sorts list in preparation for reducing step
    '''
    startBook = False
    totalWords = 0
    fullArray = []
    output = ''
    file = open(file)
    for line in file.readlines():
        if line.find("*** START OF THIS PROJECT GUTENBERG EBOOK") != -1:
            startBook = True
        elif line.find("*** END OF THIS PROJECT GUTENBERG EBOOK") != -1: #reached end of ebook, so stop adding lines
            startBook = False           
        elif startBook and line.find("*** START OF THIS PROJECT GUTENBERG EBOOK") == -1 and len(line) > 1:
            cleanedLine = line.strip()
            words = cleanedLine.split()
            modifiedWords = []
            for word in words:
                word = word.translate(string.maketrans("",""), string.punctuation).lower() #used code at following link: http://stackoverflow.com/questions/265960/best-way-to-strip$
                if word != "":
                    modifiedWords = modifiedWords + [word]
                    totalWords = totalWords + 1
            fullArray = fullArray + modifiedWords
    for element in sorted(fullArray):
        output = output + element+",1\n"
    with open('output.txt', 'w') as f:
        f.write(output)
    return 'output.txt'


def reducer(file):
    '''
    Reduces the file produced by stringManipulationPG.py, returning a single total for each token. 
    Returns output in plain text file, 'output.txt'. 
    Code recycled from INLS690: Intro to Big Data & NoSQL (modified delimeter from "\t" to ",")
    '''
    output = ''
    (last_key, sum_val) = (None, 0)
    file = open(file)
    for line in file.readlines():
        (key, val) = line.strip().split(",") #was \t
        if last_key and last_key != key:
            output = output + last_key+","+str(sum_val)+"\n"
            (last_key, sum_val) = (key, int(val))
        else:
            (last_key, sum_val) = (key, sum_val + int(val))

    if last_key:
        output = output + last_key+","+str(sum_val)+"\n"
    with open('output.txt','w') as f:
        f.write(output)
    return 'output.txt'

def printTopWords(file): 
    '''
    Finds top 20 most frequently occurring terms in a file. 
    Input file expected to come from reducer.py output. Returns output in plain text file, 'output.txt'. 
    '''
    fullArray = []
    numArray = []
    lowest = 0
    topItem = ''
    file = open(file)
    for line in file.readlines():
        line = line.strip()
        fullArray = fullArray + [line]
    for element in sorted(fullArray):
        numArray = numArray + [int(element[element.find(",")+1:])]
    numArray.sort(reverse=True)
    print numArray[0:19]
    for element in fullArray:
        for num in numArray[0:19]:
            if int(element[element.find(",")+1:]) == num:
                if element in fullArray:
                    fullArray.remove(element)
                    print element

def checkForWords(file):
    '''
    Compares words in an input document file to a master word list, 'words.txt'. 
    Prints words that are not present
    '''
    file = open(file)
    allWords = open('words.txt')
    dictionary = [line.rstrip('\r\n') for line in allWords] #modified code found here: http://stackoverflow.com/questions/14535619/remove-line-break-from-each-element-in-python
    for line in file.readlines():
        line = line.strip()
        words = line.split()
        for word in words:
            word = word[0:word.find(",")]
            found = False
            index = 0
            for element in dictionary:
                if found:
                    break
                if word == element:
                    found = True
                    break
                elif word != element and index < len(dictionary)-1:
                    index = index + 1
                else:
                    print "The word " + word + " is not in the dictionary"
                    break

def readFile(file):
    '''
    used to print output files
    '''
    file = open(file)
    for line in file.readlines():
        line = line.strip()
        print line


print process_file('book.txt')
readFile(reducer(process_filePG('book.txt')))
printTopWords(reducer(process_filePG('book.txt')))
checkForWords(reducer(process_filePG('book.txt')))