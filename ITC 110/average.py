#average.py
#compute the average of two numbers

def main():
    print("Let's compute the average of two numbers")

    num1, num2 = eval(input("Enter the first number, then the second number sperated by a comma: "))
    average = (num1 + num2) / 2
    print("The average of", num1, "and", num2, ", is :", average)

main()
