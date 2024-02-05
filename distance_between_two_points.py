# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

def calculate_distance_between_two_circles(xc1, yc1, xc2, yc2):
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

def calculate_vector_length(xa, ya, xb, yb):
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

def main():
    xc1 = 4
    yc1 = 4.25

    xc2 = 53
    yc2 = -5.35

    xa = -36
    ya = 97

    xb = .34
    yb = .91

    print('distance between two circles:', calculate_distance_between_two_circles(xc1, yc1, xc2, yc2))
    print('Lengh of vector:', calculate_vector_length(xa, ya, xb, yb))

main()