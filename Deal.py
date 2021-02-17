# File: Deal.py

# Description: Simulates the Monty Hall problem and calculates the success of the strategy of switching doors for a user defined number of trials

# Student Name: Jack Gammack

# Student UT EID: jg64475

# Course Name: CS 303E

# Unique Number: 51345

# Date Created: 10/20/2017

# Date Last Modified: 10/20/2017

import math
import random

def main():

    #number of times to play
    n = int(input('Enter number of times you want to play: '))
    print()
    print('  Prize      Guess       View    New Guess ')
    
    #wins by switching
    wbs=0

    #repeat n times
    for trial in range(0,n):
        
        prize = random.randint(1,3)
        guess = random.randint(1,3)

        #assign view to a number [1,3] that is neither prize nor guess
        view=1
        while(view==prize or view==guess):
            view+=1

        #assign newGuss to a number [1,3] that is neither view nor guess
        newGuess=1
        while(newGuess==view or newGuess==guess):
            newGuess+=1

        #increase wins if newGuess is correct
        if(newGuess==prize):
            wbs+=1
        print('    ' + str(prize) + '          ' + str(guess) + '          ' +str(view) + '          ' + str(newGuess) )

    print()
    print( 'Probability of winning if you switch = ' + str(format(wbs/n,'.2f')))
    print( 'Probability of winning if you do not switch = ' + str(format(1-wbs/n,'.2f')))
       
main()        
        
        
        
