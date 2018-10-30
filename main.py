from support.webClass import Web

def getName():
    return str(input("\nEnter the file of .HTML file -> "))

def bye():
    print("\n!--Thanks for using this product--!\n")

def main():
    web = Web(getName())
    web.checkFile()
    web.getUserSpeech()
    if str(input("Enter 'X' to exit or Enter anything to continue : ")) == "X":
        bye()
    else:
        main()

main()