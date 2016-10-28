import random
import string


def process_file(filename, skip_header):
    """
    Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """
    Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def most_common(hist):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=1000):
    """
    Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    # print('The most common scary words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def compare(hist, scarywords):
    """
    If word in book matches word in book, keep that word.

    book, scarywords: dictionaries
    """
    new = {}
    # hist = most_common(hist)
    for key in scarywords:
        if key in hist:
            new[key] = hist.get(key, 0)
    return new

scarywords = process_file('horrorkeywords.txt', skip_header=False)
book = process_file('poe1.txt', skip_header=True)

def main():
    hist = process_file('poe1.txt', skip_header=True)
    scarywords = list(process_file('horrorkeywords.txt', skip_header=False).keys())
    t = compare(hist,scarywords)
    print('The most common scary words are:' )
    print_most_common(t ,num = 200)


if __name__ == '__main__':
    main()