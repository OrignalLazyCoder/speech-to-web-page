from support.webClass import Web

def getName():
    return str(input("\nEnter the file of .HTML file -> "))

def main():
    web = Web(getName())
    web.checkFile()
    web.getUserSpeech()

main()