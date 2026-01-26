#input =12 
#output=16 1+2+3+4+6

def Number(Num):
    Sum=0

    for i in range(1,Num,1):
        if(Num%i==0):
            Sum=i+Sum
            

    return Sum

    
def main():

    print("Enter number :")
    No=int(input())

    ret=Number(No)

    print("addition of factors are :",ret)


if __name__ =="__main__":
    main()
