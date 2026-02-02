#Display file contain line by line on screen

import sys

def LinebyLine(File1):
    
    count=0
    fobj=open(File1)
    for _ in fobj:
        print(_,end='')

def main():
    
    if len(sys.argv) !=2:
        print("Specify the name of file")
        return
    

    LinebyLine(sys.argv[1])

    

if __name__ == "__main__":
    main()
