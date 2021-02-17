#  File: Benford.py

#  Description: Reads 2009 census data and prints the distribution of leading digits of populations

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 11/28/2017

#  Date Last Modified: 11/29/2017

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  total = 0
  for line in in_file:
    total += 1
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = int(pop_data[-1])
    while( pop_num > 9 ):
        pop_num = pop_num//10
    pop_freq[ str(pop_num) ] += 1;

    # make entries in the dictionary
    
  # close the file
  in_file.close()

  # write out the result
  print( 'Digit   Count   %' )
  print( '1       ' + str(pop_freq['1']) + '    ' + str(round(pop_freq['1']/total*100,1)))
  print( '2       ' + str(pop_freq['2']) + '    ' + str(round(pop_freq['2']/total*100,1)))
  print( '3       ' + str(pop_freq['3']) + '    ' + str(round(pop_freq['3']/total*100,1)))
  print( '4       ' + str(pop_freq['4']) + '    ' + str(round(pop_freq['4']/total*100,1)))
  print( '5       ' + str(pop_freq['5']) + '    ' + str(round(pop_freq['5']/total*100,1)))
  print( '6       ' + str(pop_freq['6']) + '    ' + str(round(pop_freq['6']/total*100,1)))
  print( '7       ' + str(pop_freq['7']) + '    ' + str(round(pop_freq['7']/total*100,1)))
  print( '8       ' + str(pop_freq['8']) + '    ' + str(round(pop_freq['8']/total*100,1)))
  print( '9       ' + str(pop_freq['9']) + '     ' + str(round(pop_freq['9']/total*100,1)))
  
  
  
main()
