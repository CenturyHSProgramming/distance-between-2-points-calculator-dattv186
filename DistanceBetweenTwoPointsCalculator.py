# DistanceBetweenPointsCalculator.py
# Your job is to write a function in DistanceBetweenPointsCalculator.py (call
# it **calculateDistanceBetween()** that calculates the distance between two points
# in 2D space (x1, y1) and (x2, y2)
# based on The Distance Formula
# mathwarehouse.com (http://www.mathwarehouse.com/algebra/distance_formula/index.php)

# Define Function below
# be sure to return an integer

import math


def calculateDistanceBetween(x1, y1, x2, y2):
    calculateDistanceBetween = ((x2 - x1)**2) + ((y2 - y1)**2)
    from math import sqrt as square_root
    calculateDistanceBetween = square_root(calculateDistanceBetween)
    calculateDistanceBetween = round(float(calculateDistanceBetween), 2)
    return(calculateDistanceBetween)







if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented

    x1 = int(input('Enter a number for x1:    '))
    x2 = int(input('Enter a number for x2:    '))
    y1 = int(input('Enter a number for y1:    '))
    y2 = int(input('Enter a number for y2:    '))
    distance = calculateDistanceBetween(x1, y1, x2, y2)
    print(distance)
    
    
             
