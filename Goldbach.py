#  File: Goldbach.py

#  Description: Verifies Goldbach's conjecture in a user defined range

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/12/2017

#  Date Last Modified: 10/13/2017

def is_prime (n):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

def main():
    lower=0
    upper=0
    while( lower<4 or lower%2!=0 or upper%2!=0 or lower>=upper):
        lower=int(input('Enter the lower limit: '))
        upper=int(input('Enter the upper limit: '))
    for total in range(lower,upper+1,2):
        ans=str(total)
        for first in range(2,int(total/2+1)):
            if( is_prime(first) and is_prime(total-first) ):
                ans+= ' = ' + str(first) + ' + ' + str(total-first)
        print(ans)
main()
    
