#check even or odd

def ChkNum(Num):

    if Num%2==0:
        return True
    
    else:
        return False


def main():
    
    print("Enter number :")
    No=int(input())

    ret=ChkNum(No)

    if(ret==True):
        print("Even number")

    else:
        print("Odd Number ")



if __name__ =="__main__":
    main()
