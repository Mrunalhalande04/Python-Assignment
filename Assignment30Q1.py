#count new  lines in file

import sys

def CopyFile(File1):
    
    count=0
    file=open(File1)

    for _ in file:
        count=count+1

    return count

def main():
    
    if len(sys.argv) !=2:
        print("Specify the name of file")
        return
    

    ret=CopyFile(sys.argv[1])

    print("Total number of new lines are ",ret)

if __name__ == "__main__":
    main()
