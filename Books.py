#  File: Books.py

#  Description: Compares the vocabularies of Charles Dickens and Thomas Hardy

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 12/4/2017

#  Date Last Modified: 12/5/2017

# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
    in_file = open('words.txt','r')
    for line in in_file:
        word_dict[line.strip()] = 1
    in_file.close()

# Removes punctuation marks from a string
def parseString (st):
    ans = ''
    st.strip()
    for i in range(0,len(st)):
        if ( i>1 and st[i-1:i+1] == '\'s' ):
            continue
        if ( st[i].isalpha() or st[i].isspace() ):
            ans += st[i]
        elif ( st[i]=='!' or st[i]=='#' or st[i]=='$' or st[i]=='%' or st[i]=='&' or st[i]=='(' or st[i]==')' or st[i]=='-' or st[i]=='?' or st[i]=='/' or st[i]=='.' or st[i]==',' or st[i]=='\"' or st[i]==';' or st[i]==':' ):
            ans += ' '
        elif ( i+1<len(st) and st[i] == '\'' and st[i+1] == ' ' ):
            ans = ans
        elif ( i+1<len(st) and st[i:i+2] == '\'s' ):
            ans = ans
        elif ( st[i].isdigit() ):
            ans = ans
        else:
            ans += st[i]
    return ans

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
    Book = open(file,'r')
    dict = {}
    for line in Book:
        st = parseString(line)
        words = st.split()
        for item in words:
            if ( item in dict ):
                dict[item] += 1
            else:
                dict[item] = 1
    Book.close()
    caps = {}
    for key in dict:
        if ( key[0].isupper() ):
            caps[key] = dict[key]
    for key in caps:
        if ( key.lower() in dict ):
             dict[ key.lower() ] = dict[ key.lower() ] + caps[key]
        elif ( key.lower() in word_dict ):
             dict[ key.lower() ] = caps[key]
        del dict[key]
    return dict
    
        
  
# Compares the distinct words in two dictionaries
def wordComparison (book1, author1, book2, author2):
    dictT = getWordFreq(book1)
    dictR = getWordFreq(book2)
    print( author1 )
    print( 'Total distinct words = ' + str( len(dictT) ) )
    print( 'Total words (including duplicates) = ' + str( sum( list( dictT.values() )) ) )
    print( 'Ratio (% of total distinct words to total words) = ' + str( round(len(dictT) / sum( list( dictT.values() )) * 100,10) ) )
    print()
    print( author2 )
    print( 'Total distinct words = ' + str( len(dictR) ) )
    print( 'Total words (including duplicates) = ' + str( sum( list( dictR.values() )) ) )
    print( 'Ratio (% of total distinct words to total words) = ' + str( round(len(dictR) / sum( list( dictR.values() )) * 100,10) ) )
    print()
    D = set( dictT.keys() )
    H = set( dictR.keys() )
    print( author1 + ' used ' + str( len( D-H ) ) + ' words that ' + author2 + ' did not use.' )
    sumDH = 0
    for elt in D-H:
        sumDH += dictT[elt]
    print( 'Relative frequency of words used by ' + author1 + ' not in common with ' + author2 + ' = ' + str( round(sumDH / sum( list( dictT.values() )) *100,10) ) )
    print()
    print( author2 + ' used ' + str( len( H-D ) ) + ' words that ' + author1 + ' did not use.' )
    sumHD = 0
    for elt in H-D:
        sumHD += dictR[elt]
    print( 'Relative frequency of words used by ' + author2 + ' not in common with ' + author1 + ' = ' + str( round(sumHD / sum( list( dictR.values() )) *100,10) ) )

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (book1, author1, book2, author2)
  
main()
