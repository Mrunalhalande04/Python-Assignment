#check number is divisible by 5 or not

def ChkNum(Num):

    if Num%5==0:
        return True
    
    else:
        return False


def main():
    
    print("Enter number :")
    No=int(input())

    ret=ChkNum(No)

    if(ret==True):
        print("number is divisible by 5 ..")

    else:
        print("number is not divisible by 5.. ")



if __name__ =="__main__":
    main()
