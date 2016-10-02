#GAME OF NIM 
from random import randrange

"""
I pre-calculated a list of powers of 2 - 1 instead of calculating each time
"""
power_of_two = [3,7,15,31,63]

def nim():
    """
    Plays the game of Nim with the user - the pile size, AI intelligence and starting user are randomly determined
    Returns True if the user wins, and False if the computer wins
    """
    #generates the pile size 
    pile_size = randrange(10,101)
    #decides who gets to go first: 0 is computer, 1 is human
    start = randrange(0,2)
    #decides whether the computer's strategy is dumd or stupid: 0 is dumb and 1 is smart
    comp_strategy = randrange(0,2)

    print('The game begins! The pile size is %s marbles.' %(pile_size))
    
    if comp_strategy == 0:
        print('You are lucky! The computer is dumb')
    else:
        print('The computer is smart. Good luck to you.')

    #create loop that breaks when the pile size is 2
    while pile_size > 2:
        #defining the computer's move
        if start == 0:
            print('It is my turn')
            #defining the computer's move based in its strategy
            #the computer will take a random amount only when it is dumb or if the pile size is a power of 2 - 1
            if comp_strategy == 0 or pile_size in power_of_two:
                computer_take = randrange(1, pile_size // 2 + 1)
            #the computer will make the pile a number in the list of power of 2 - 1 a legal move if it is smart
            else:
                for power in power_of_two:
                    #checks which power of 2 - 1 can be made in the legal move
                    if (pile_size // 2 >= pile_size - power) and (pile_size - power > 0):
                        #the computer makes its move 
                        computer_take = pile_size - power
                        break
            pile_size -= computer_take
            print('I take %d marbles from the pile. The pile now has %d marbles' %(computer_take,pile_size))
            #chance to the human's turn
            start = 1
        else:
            #prevents the human from having a turn if the pile size is 2 because the game is over
            if pile_size == 2:
                break
            print('It is your turn')
            human_take = 0
            #forces the human to input a valid integer as their move
            while human_take < 1 or human_take > pile_size // 2:
                human_take = int(input('Please enter an integer between 1 and %d: ' %(pile_size // 2)))
            pile_size -= human_take
            print('You have taken %d marbles from the pile. The pile is has %d now' %(human_take, pile_size))
            #changes back to the computer's turn 
            start = 0

    #uses the most recent turn to decide the winner of the game
    #the winner is whoever takes one marble from a pile size of 2
    if start == 0:
        print('I take one marble from the pile and leave you with the last one. You have lost.')
        return False
    else: 
        print('You take one marble from the pile and leave me with the last one. You win!!')
        return True

nim()