"""
#EXERCISE ONE:
prefixes = ["J","K","L","M","Ou","P","Qu"]
suffix = 'ack'
print(prefixes + suffix)

#EXERCISE TWO:
def character_count(my_string, a):
    answer = 0
    for letter in my_string:
        if letter == a:
            answer += 1
    return answer
"""
"""
#EXERCISE THREE WAS READING AND EXPERIMENTING

#EXERCISE FOUR
def word_value(word):
    total = 0
    for letter in word:
        total += ord(letter) - 96
    return total

def paperthing(my_list):
    max_length = 0
    for word in my_list:
        if len(word) > max_length:
            max_length = len(word)
    grand_total = 0
    for word in my_list:
        print('{:{align}{width}}'.format(word, align='<', width=str(max_length+4))+'{:{align}{width}}'.format('$'+ str(word_value(word)), align='>', width='5'))
        grand_total += word_value(word)
    print('------------------------')
    print('{:{align}{width}}'.format('Total', align='<', width=str(max_length+4))+'{:{align}{width}}'.format('$'+ str(grand_total), align='>', width='5'))

the_list = ['bananas', 'rice', 'paprika', 'potato chips']

paperthing(the_list)
"""
"""
#EXERCISE FIVE

The first function only returns true or false of the first letter, and then stops

The second function checks the letter 'c' instead of the string stored in c, and it returns a string 'true' or 'false' instead of the True or False operators

The third function only returns whether the last character is lowercase, because the flag variable keeps being reassigned

The fourth function works for the intended purpose - if any character is found to be True, flag will be assigned True, and by the 'or'' statement will always be True thereafter

The fifth function doesn't work because any character found to be not lowercase will return False and stop the function
"""
""""
#EXERCISE SIX
def rotate_word(my_word, rotate):
    final_string = ''
    for character in my_word:
        if character.isalpha():
            new_letter = chr((ord(character.lower()) - 97 + rotate) % 26 + 97)
            final_string += new_letter
        else:
            final_string += character
    return final_string
"""

"""
#CUBE BISECTION
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
"""
"""
cube = 27
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))
"""

