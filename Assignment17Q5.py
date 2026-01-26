#chk prime or not



def ChkPrime(Num):

    
    for i in range(2,Num,1):
        if(Num%i==0):
            return False
        
    
    return True


def main():
    
    print("Enter number :")
    No=int(input())

    ret=ChkPrime(No)

    if(ret==True):
        print("Prime Number")

    else:
        print("Not Prime Number ")



if __name__ =="__main__":
    main()
