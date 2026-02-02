#Display data on console

import sys

def CopyFile(FileName):

    fobj=open(FileName)
    data=fobj.read()
    fobj.close()

    ffobj=open("Hello.txt","w")
    ffobj.write(data)
    ffobj.close()

def main():
    
 #   if len(sys.argv) !=2:
  #      print("Specify the name of file")
   #     return
    

    CopyFile(sys.argv[1])
    print("File copied successfully")

if __name__ == "__main__":
    main()
