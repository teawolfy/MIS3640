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