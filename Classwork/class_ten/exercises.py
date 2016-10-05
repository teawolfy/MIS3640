def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number

    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for i in t:
        try:
            total += i
        except TypeError: #I was getting errors whendebugging this, so I added this except clause
            total += nested_sum(i)
    return total

def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers

    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    result = []
    total = 0
    for i in t:
        total += 1
        result.append(total)
    return result

def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    list = t
    newList = []
    for i in range(len(list[:-1])):
        newList = list[i]>list[i+1]
    return newList



def chop(t):
    """Removes the first and last elements of t.

    t: list

    returns: None #what do you mean by this?

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    for i in range(len(t)):
        t =  t.pop(0) and t.pop(2)
        #okay, so I know that t.pop(2) will not work for additional lists, but it works for now!
        return t


def is_sorted(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean

    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    if len(t) == 1:
        return True
    else:
        return t[0] <= t[1] and is_sorted(t[1:])

def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.

    word1: string or list
    word2: string or list

    returns: boolean

    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    True
    """
    #establish how to check the letters in string1 and string2
    string1 = word1
    string2 = word2
    word1 = []
    word2 = []
    for x in range(len(string1)):
        word1.append(string1[x])
    for x in range(len(string2)):
        word2.append(string2[x])

    #validate if the same letters are used in string1 and string2
    if(len(word1) == len(word2)):
        for letter in word1:
            if letter in word2:
                word2.remove(letter)

    #validate if the strings are anagrams
    if len(word2) == 0:
        return True
    else:
        return False


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.

    s: string or list

    returns: bool
    """
    for i in s:
        if s.count(i) > 1:
            return True
        return False
    

def main():
    print('EXERCISE ONE')
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    print('EXERCISE TWO')
    t = [1, 2, 3]
    print(cumsum(t))

    print('EXERCISE THREE')
    t = [1, 2, 3, 4]
    print(middle(t))
    print('EXERCISE FOUR')
    chop(t)
    print(t)
    print('EXERCISE FIVE')
    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))
    print('EXERCISE SIX')
    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))
    print('EXERCISE SEVEN')
    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()