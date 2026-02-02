#check wthere file contain word or not


import sys

def copyfile(File1,word):
    
    fobj=open(File1,"r")
    robj=fobj.read()
    
    for i in robj:
        data=i.split
        if(data==word):
            return True
        else:
            return False
    
def main():
    
    if len(sys.argv) !=3:
        print("Specify the name of file")
        return
    

    ret=copyfile(sys.argv[1],sys.argv[2])

    if ret==True:
        print("word found")

    else:
        print("word does not found")

    

if __name__ == "__main__":
    main()
