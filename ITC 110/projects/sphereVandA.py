#sphereVandA
#This program finds the volume and surface area of a sphere

import math

def main():
    r = int(input("Enter a whole number: "))
    vol = 4/3 * math.pi * r**3
    print("Volume if:", vol)
    area = 4 * math.pi * r**2
    print("Surface area is:", area)

    
main()
