#  File: Spiral.py

#  Description: Prints out the neighbouring numbers of a given number in a number spiral of given dimension

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/16/2017

#  Date Last Modified: 11/20/2017

def main():
    dim = int( input('Enter dimension: ') )
    num = int( input('Enter number in spiral: ') )
    print()

    #Check to make sure num is in spiral
    if ( num<1 or num > dim**2 ):
        print('Number not in Range')
        return

    #Fill dim x dim grid with zeroes
    grid = [[0 for col in range(dim)] for row in range(dim)]

    #Set center value to 1
    row = dim//2
    col = dim//2
    n = 2
    grid[dim//2][dim//2] = 1
    curr = 1;

    #Grid filling magic, moves right 1, down 1, left 2, up 2, right 3
    #, down 3, ...
    #Breaks the loop if we have reached the last number
    while( n<=dim**2 ):
        for r in range(1,curr+1):
            grid[row][col+1] = n
            col+=1
            n+=1
            if ( n-1==dim**2 ):
                break

        if ( n-1==dim**2 ):
                break
        
        for d in range(1,curr+1):
            grid[row+1][col] = n
            row+=1
            n+=1
        
        curr+=1
        for l in range(1,curr+1):
            grid[row][col-1] = n
            col-=1
            n+=1
        
        for u in range(1,curr+1):
            grid[row-1][col] = n
            row-=1
            n+=1
        curr+=1
        
    #Find index of num
    for ro in range(0,dim):
        if ( grid[ro].count(num) > 0 ):
            c = grid[ro].index(num)
            r = ro
            
    #Find if num is on outer edge
    if ( r == 0 or r == dim-1 or c == 0 or c == dim-1 ):
        print( 'Number on Outer Edge')
        return
    #Print out square around num
    else:
        print( grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1] )
        print( grid[r][c-1], grid[r][c], grid[r][c+1] )
        print( grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1] )

main()
