#kilo2mile.py

def main():
    print("This program converts distances measured in kilometers into miles.")
    
    #grab user input
    km = eval(input("Please enter a distance in kilometers: "))
    
    #convert user input to miles
    miles = km * 0.62
    
    #print the converted value
    print(km, "kilometers is equivalent to about", round(miles, 2),"miles")

main()
