from support.webClass import Web

def getName():
    return str(input("Enter the file of .HTML file -> "))

def main():
    web = Web(getName())
    web.checkFile()

main()