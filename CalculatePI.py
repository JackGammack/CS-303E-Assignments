#  File: CalculatePI.py

#  Description: Calculates pi using area of a square and an inscribed circle

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/16/2017

#  Date Last Modified: 10/17/2017

import math
import random

def computePI( numThrows ):

    numIn=0
    for throw in range(0,numThrows):
        xPos = random.uniform(-1.0,1.0)
        yPos = random.uniform(-1.0,1.0)
        if( xPos**2 + yPos**2 <= 1 ):
            numIn+=1
    return round(4*numIn/numThrows,6)

def main():

    cPi=computePI(100)
    if(cPi-math.pi>0):
        print('num = ' + str(100) + '        Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = +' + str(format(cPi-math.pi,'.6f')))
    else:
        print('num = ' + str(100) + '        Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = ' + str(format(cPi-math.pi,'.6f')))
    cPi=computePI(1000)
    if(cPi-math.pi>0):
        print('num = ' + str(1000) + '       Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = +' + str(format(cPi-math.pi,'.6f')))
    else:
        print('num = ' + str(1000) + '       Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = ' + str(format(cPi-math.pi,'.6f')))
    cPi=computePI(10000)
    if(cPi-math.pi>0):
        print('num = ' + str(10000) + '      Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = +' + str(format(cPi-math.pi,'.6f')))
    else:
        print('num = ' + str(10000) + '      Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = ' + str(format(cPi-math.pi,'.6f')))
    cPi=computePI(100000)
    if(cPi-math.pi>0):
        print('num = ' + str(100000) + '     Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = +' + str(format(cPi-math.pi,'.6f')))
    else:
        print('num = ' + str(100000) + '     Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = ' + str(format(cPi-math.pi,'.6f')))
    cPi=computePI(1000000)
    if(cPi-math.pi>0):
        print('num = ' + str(1000000) + '    Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = +' + str(format(cPi-math.pi,'.6f')))
    else:
        print('num = ' + str(1000000) + '    Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = ' + str(format(cPi-math.pi,'.6f')))
    cPi=computePI(10000000)
    if(cPi-math.pi>0):
        print('num = ' + str(10000000) + '   Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = +' + str(format(cPi-math.pi,'.6f')))
    else:
        print('num = ' + str(10000000) + '   Calculated PI = ' + str(format(cPi,'.6f')) + '   Difference = ' + str(format(cPi-math.pi,'.6f')))

main()
