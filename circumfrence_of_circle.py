#!/usr/bin/env python3

# Created by: Lauren
# Created on: April 2021
# This program calculates the area and perimeter of a rectangle
#    with length and width inputted from the user

import constants


def main():
    # this function calculates the circumfrence of a circle

    # print("Enter the radius of the circle")
    r = int(input("Enter the radius of a circle "))
    print("The circumfrence is {}".format(r*constants.TAU))


if __name__ == "__main__":
    main()
