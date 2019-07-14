#change.py

def main():
    print("This program calculates dollar amount from number or coins")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    dollarAmount = quarters/4 + dimes/10 + nickels/20 + pennies/100
    print("The total dollar amount is:", "$" + str(round(dollarAmount, 2)))

main()
