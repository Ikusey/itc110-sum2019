#hello.py

def hello(personName):
    print("Hello,", personName + ", how are you?")

def main():
    #get user input
    person = input("Enter your name: ")
    hello(person)

main()
