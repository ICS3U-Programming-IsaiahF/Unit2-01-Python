#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: September 20, 2022
# This program calculates the area and perimeter of a circle.


import math

def main():
    #This function calculates area and perimeter. 
    R=6
    print("if a circle has a radius of:")
    print("{}cm". format(R))
    print("")
    print("Area is {}cm^2". format(math.pi*R**2))
    print("Perimeter is {}cm". format(math.pi*R*2))


if __name__ == "__main__":
    main()