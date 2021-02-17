#  File: EasterSunday.py

#  Description: Given a year, calculates Easter Sunday for that year

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 9/15/2017

#  Date Last Modified: 9/15/2017

def main():

  #prompt user for year
  y=int(input('Enter year: ')) 

  #Print empty line for spacing
  print()

  #Calculations
  a=y%19
  b=y//100; c=y%100
  d=b//4; e=b%4
  g=(8*b+13)//25
  h=(19*a+b-d-g+15)%30
  j=c//4; k=c%4
  m=(a+11*h)//319
  r=(2*e+2*j-k-h+m+32)%7
  n=(h-m+r+90)//25
  p=(h-m+r+n+19)%32

  #If in March
  if(n==3):
    print('In', y, 'Easter Sunday is on', p, 'March.')

  #If in April
  if(n==4):
    print('In', y, 'Easter Sunday is on', p, 'April.')

  #Just to check for errors
  if(n!=3 and n!=4):
    print('Error')
    
main()
