#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This program calculates the area and the perimeter of a rectangle
#    with dimensions inputted by user

import math


def main():
    # input
    length = int(input("Enter length of rectangle in mm: "))
    width = int(input("Enter width of rectangle in mm: "))

    # process
    area = length * width
    perimeter = 2 * (length + width)
    # output

    print("")
    print("The Area is: {} mm²".format(area))
    print("")
    print("The Perimeter is: {} mm".format(perimeter))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
