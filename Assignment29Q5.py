#Compare both file data

import sys

def ComFile(File1,File2):

    fobj=open(File1)
    data1=fobj.read()
    fobj.close()

    ffobj=open(File2)
    data2=ffobj.read()
    ffobj.close()
    
    if(data1 == data2):
        return True
    else:
        return False
    
   

def main():
    
    if len(sys.argv) !=3:
        print("Specify the name of file")
        return
    

    ret=ComFile(sys.argv[1],sys.argv[2])

    if(ret==True):
        print("Success")

    else:
        print("Failure")
    

if __name__ == "__main__":
    main()
