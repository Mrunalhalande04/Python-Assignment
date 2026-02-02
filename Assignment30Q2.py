#Count words in file

import sys

def Countwords(File1):
    
    count=0
    fobj=open(File1)
    data=fobj.read()
    count=data.split()

    return len(count)

def main():
    
    if len(sys.argv) !=2:
        print("Specify the name of file")
        return
    

    ret=Countwords(sys.argv[1])

    print("Total number of words are ",ret)

if __name__ == "__main__":
    main()
