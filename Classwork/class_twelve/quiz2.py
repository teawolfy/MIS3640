# Upload quiz_2.py file to Blackboard - Session 12


def replace_even(data):
    '''
    Replace all elements at an even index in the list with 0.
    No return is required.

    data: the list of values to process'''
    for n,i in enumerate(data):
        if i % 2 == 0:
            data[n] = 0
            
        
# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN)


def remove_middle(data):
    '''
    Remove the middle element if the list length is odd,
    or the middle two elements if the list length is even.  
    No return is required.

    data: the list of values to process
    '''
    for i in range(len(data)):
        if len(data) % 2 == 0:
            data.pop(5)
        #else:
            #data.pop(5) and data.pop(6)
        

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN)


def insert_integer(data, number):
    '''
    given a sorted list of integers, insert a new integer into
    its proper position so that the new list stays sorted. 
    Do not use sort function or sorted function inside this function.

    data: a list of integers
    number: a new integer

    return: a new list of sorted integers with previous numbers and 
    the new number
    '''
    new_data = []

    for i in data:
        new_data = data.insert(i, len(data)-1) and data.sort(data)
    return new_data

# Uncomment the following lines to test
data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
new_data = insert_integer(data, 2015)
print(new_data)


def print_hist(data):
    '''
    given a dictionary of letter: positive integer pairs, 
    print rows with the letter and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.

    data: a dictionary of letter: positive integer pairs

    Example:
    letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
    print_hist(letter_counts)

    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********

    '''
    key_list = list(data.keys())
    key_list.sort()
    for key in key_list:
        num_ast = data.get(key)
        print('%s: ' %(key) + num_ast())
        
letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}    
print_hist(letter_counts)
