#Display file contain line by line on screen

import sys

def copyfile(File1,File2):
    
    fobj=open(File1,"r")
    Data1=fobj.read()
    fobj.close()

    ffobj=open(File2,"w")
    ffobj.write(Data1)
    ffobj.close()

    print("contain successfully copied")

def main():
    
    if len(sys.argv) !=3:
        print("Specify the name of file")
        return
    

    copyfile(sys.argv[1],sys.argv[2])

    

if __name__ == "__main__":
    main()
