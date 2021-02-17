#  File: ISBN.py

#  Description: Reads a list of ISBN numbers and determines their validity

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/26/2017

#  Date Last Modified: 10/30/2017

def main():

    #Open file for reading
    in_file = open('./isbn.txt', 'r')
    out_file = open('./isbnOut.txt', 'w')

    for line in in_file:
        valid=True
        digits=[]
        s1=[]
        s2=[]
        ISBNnum = line.strip()

        #Check for any bad characters, create list of digits
        for char in ISBNnum:
            #Check for bad characters
            if( char!='X' and char!='x' and char!='-' and not( ord(char)>=48 and ord(char)<=57 ) ):
                valid = False
                break
            #Add each non-hyphen character to digits
            if( char!='-' ):
                digits.append(char)

        #Check that digits is correct length
        if( valid and len(digits)!=10 ):
            valid = False

        #Check to make sure 'X' or 'x' is only in the last position of the ISBN
        #Convert 'X' or 'x' to '10'
        #Convert the characters in digits to ints
        for i in range(0,10):
            if( valid and i!=9 and (digits[i]=='x' or digits[i]=='X') ):
                valid=False
            if( valid and (digits[i]=='x' or digits[i]=='X') ):
                digits[i]=10
            if( valid ):
                digits[i] = int(digits[i])

        #Create s1 and s2    
        if( valid ):
            s1.append( digits[0] )
            s2.append( s1[0] )
            for i in range(1,10):
                s1.append(s1[i-1]+digits[i])
                s2.append(s2[i-1]+s1[i])

        #Check if s2 is divisible by 11
        print(s2)
        if( valid and s2[9]%11 != 0 ):
            valid=False

        #Write to file
        if( valid ):
            out_file.write( ISBNnum + ' valid' + '\n') 
        if( not valid):
            out_file.write( ISBNnum + ' invalid' + '\n')
        
    

main()
    
