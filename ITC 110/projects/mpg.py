#mpg.py

def main():
    print("This program calculates mpg based on miles driven and gas used")
    miles, gas = eval(input("Enter miles driven and gas used seperated by a comma: "))
    mpg = miles/gas
    print("Going", miles, "miles using", gas, "gallons of gas is", round(mpg, 2), "mpg")

main()
