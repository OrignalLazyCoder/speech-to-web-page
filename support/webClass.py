import speech_recognition as sr 
import os.path

class Web : 

    def __init__(self , name):
        self.name = name
        self.path = "./webpages/"+self.name+".html"

    def createFile(self):
        f = open(self.path , "w+")
        content = "<html>\n<head>\n<title>"+self.name+"</title></head><body>"
        f.write(content)
        f.close()
        print("\n!-- FILE CREATED --!\n")
        

    def checkFile(self):
        check = os.path.isfile(self.path)
        if not check:
           self.createFile()
        else:
            choice = str(input(("File Already Exist. Do you want to overwrite it ? (y/n) : ")))
            if choice is "y":
                self.createFile()
            elif choice is "n":
                print("\n!--WEB DEVELOPMENT ABORTED --!\n")
            else:
                self.checkFile()