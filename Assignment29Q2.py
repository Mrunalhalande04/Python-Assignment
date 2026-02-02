import os

def OpenFile(FileName):

    fobj=open(FileName,"r")
    Data=fobj.read()
    print("File data is :",Data)
    

def main():
    name = input("Enter file name that you want to open ")
    OpenFile(name)

if __name__ == "__main__":
    main()
