#quadratic.py
import math
def rootQuad(a, b, c):
    discRoot = math.sqrt(b*b-4*a*c)
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b - discRoot) / (2*a)
    print("The solutions are: ", root1, root2)

def main():
    print("Enter 3 coefficients")
    a = int(input("Coefficient 1: "))
    b = int(input("Coefficient 2: "))
    c = int(input("Coefficient 3: "))
    rootQuad(a, b, c)

main()
