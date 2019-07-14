#moleWeight.py
#This program calculates the molecular weight of a carbohydrate
#(in grams per mole) based on the number of hydrogen, carbon and oxygen atoms

def main():
    print("Please enter the number of hydrogen, carbon and oxygen atoms in the molecule")
    hydro = float(input("Hydrogen atoms: ")) * 1.00794
    carb = float(input("Carbon atoms: ")) * 12.0107
    oxy = float(input("Oxygen atoms: ")) * 15.9994

    moleWeight = hydro + carb + oxy

    print("The weight of the molecule is:", moleWeight)

main()
