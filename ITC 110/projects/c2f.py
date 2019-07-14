#convert Celsius temps to Fahrenheit

def main():
    #grab user input
    celsius = eval(input("Enter the Celsius temperature? "))

    #convert celsius to fahrenheit
    fahrenheit = 9/5 *celsius + 32
    print("The fahrenheit temperature is", fahrenheit)

main()
