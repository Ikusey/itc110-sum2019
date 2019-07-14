#factorial.py

def main():
    #get user input
    num = int(input("Enter a whole number: "))
    factor = 1
    #factor user input
    for i in range(1, num + 1):
        factor = factor * i
        print(factor)
    #print result
    print(num, "factorial is:", factor)

main()
    
