#  File: GuessingGame.py

#  Description: Uses binary search to guess the number the user is thinking of

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/15/2017

#  Date Last Modified: 11/15/2017

def main():
    print('Guessing Game')
    print()
    print('Think of a number between 1 and 100 inclusive.')
    print('And I will guess what it is in 7 tries or less.')
    print()
    lo = 1
    hi = 100
    resp = 0
    while( resp != 'y' and resp != 'n' ):
        resp = input('Are you ready? (y/n): ')
    if ( resp == 'n' ):
        print()
        print('Bye')
    else:
        n = 1
        while( n < 8 ):
            mid = (lo+hi)//2
            print()
            print( 'Guess  ' + str(n) + ' :  The number you thought was ' + str( mid ) )
            resp = input( 'Enter 1 if my guess was high, -1 if low, and 0 if correct: ' )
            while( resp != '1' and resp != '0' and resp != '-1' ):
                resp = input( 'Enter 1 if my guess was high, -1 if low, and 0 if correct: ' )
            if ( resp == '1' ):
                hi = mid
                n += 1
            elif ( resp == '-1' ):
                lo = mid
                n += 1
            elif ( resp == '0' ):
                print()
                print( 'Thank you for playing the Guessing Game.' )
                break
        if ( n == 8 ):
            print()
            print( 'Either you guessed a number out of range or you had an incorrect entry.' )

main()
            
    
