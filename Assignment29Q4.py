#occurance of string into file

import sys

def Freqstring(File1,Data):
    count=0
    fobj=open(File1)
    data1=fobj.read()

    
    count=data1.count(Data)

    return count
    

def main():
    
    if len(sys.argv) !=3:
        print("Specify the name of file")
        return
    

    ret=Freqstring(sys.argv[1],sys.argv[2])

    print(f"Count of {sys.argv[2]} is : {ret}")

    

if __name__ == "__main__":
    main()
