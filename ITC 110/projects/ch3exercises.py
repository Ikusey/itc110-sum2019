#exercises chapter 3
import math
def b2():
    n = int(input("Enter a number: "))
    equa = (n * (n-1)) / 2
    print(equa)

def c2():
    r = int(input("Enter a sphere radius: "))
    area = 4 * math.pi * r**2
    print(area)

def d2():
    r = 3
    a = 2
    b = 4
    equa = math.sqrt(r * (math.cos(a))**2 + r*(math.sin(b))**2)
    print(equa)
