#EXERCISE ONE 
def sum_all(*args):
    """
    takes any number of arguments and returns their sum
    """
    return sum(args)

#print('EXERCISE ONE')
#print sum_all(1,2,3)
#print sum_all(1,2,3,4,5)

#EXERCISE TWO 
def makedict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

def most_frequent(text):
    """
    that takes a string and prints the letters in decreasing order of frequency. 
    Find text samples from several different languages and see how letter frequency varies between languages. 
    Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies.
    """
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = makedict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter, count)

#print('EXERCISE TWO PART ONE')
text = 'Hello, Professor Li!'
most_frequent(text)

#PART TWO and THREE
from collections import defaultdict

with open('words.txt', 'r') as fd:
    words = fd.read().splitlines()

def make_anagram_dict(word_list):
    """
    Take a list of words, return a dict with a fingerprint as the key
    and the anagrams made from that fingerprint as the value 
    """
    result = defaultdict(list)
    for word in word_list:
        fp = ''.join(sorted(word))
        result[fp].append(word)

    result = {fp: result[fp] 
    for fp in result if len(result[fp]) > 1} 
    return result

anagrams = make_anagram_dict(words)

def print_anagrams(anagrams):
    """Uses a generator to call and print 5 items from mydict"""
    fp = (fp for fp in anagrams)

    print("Sample from anagram dict:")
    for i in range(1, 6):
        # call once, print twice
        fp_next = fp.next()
        print ("%s %s: " % (i, fp_next), anagrams[fp_next])
    print ("\n")

print_anagrams(anagrams)

def sort_anagrams(anagrams):
    """
    Returns a list of lists containing all anagram matches. 
    The longest list (most anagrams) is at the top
    """
    anagrams_lists = []
    for fp in anagrams:
        anagrams_lists.append(anagrams[fp])
    anagrams_lists.sort(key=len, reverse=True)

    print ("Most anagrams:")
    for i in range(0, 5):
        print ("%s %d" % ((i + 1), len(anagrams_lists[i])), anagrams_lists[i])
    print("\n")