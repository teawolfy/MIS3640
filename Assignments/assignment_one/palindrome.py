def is_palindrome(string):
    """
    the palindrome function takes a string and returns True if the string is a palindrome and False if it is not
    1. the stop value on the recursion is if the string has a length of 1 or 0
    2. if the outer characters are the same, run the palindrome function on the middle of the string (excluding the outer characters)
    3. if the outer characters are not the same, the string isn't a palindrome
    """
    if len(string) <= 1:
        return True
    elif string[0] == string[len(string)-1]:
        return is_palindrome(string[1:len(string)-1])
    else:
        return False

#test
print(is_palindrome("Teresa"))
print(is_palindrome("avid diva"))