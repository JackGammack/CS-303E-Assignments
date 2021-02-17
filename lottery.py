def main():
    import random
    computer = random.randint(0,2)
    user = int(input('scissor (0), rock (1), paper (2): '))
    choices = ['scissor', 'rock', 'paper']
    if ( user==computer+1 or (user==0 and computer==2) ):
        print ( 'The computer is ' + choices[computer] + '. You are '
               + choices[user] + '. You win.')
    elif ( computer==user+1 or (computer==0 and user==2) ):
        print ( 'The computer is ' + choices[computer] + '. You are '
               + choices[user] + '. You lose.')
    else:
        print ( 'The computer is ' + choices[computer] + '. You are '
                + choices[user] + ' too. It is a draw.')


main()
