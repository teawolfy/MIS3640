"""
#EXERCISE 1
def histogram(s):
    d = dict()
    s = ""
    for i in s:
       d.get(i, 0) + 1
    return d

h = histogram('Bookkeeper')
print(h)
"""
"""
#EXERCISE 4.1
def dictionary(s):
    words = open(words.txt)
    dict = {}
    for line in words:
        for word in line.split{}:
            dict[word]=len(word)

    words.close()
    return dictionary
"""
#EXERCISE 4.2
"""
Write a function named has_duplicates that takes a list as 
a parameter and returns True if there is any object that 
appears more than once in the list.
"""
def has_duplicates(list):
    dictionary = {}
    for item in list:
        dictionary[item] = 1 + dictionary.get(item, 0)
        if dictionary[item] > 1:
            return True
        else:
            return False

theList = [3, 4, 7, 8, 9, 0, 7]

print has_duplicates(theList)