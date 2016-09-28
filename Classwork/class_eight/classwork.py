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


#EXERCISE FIVE

#EXERCISE SIX

"""
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

