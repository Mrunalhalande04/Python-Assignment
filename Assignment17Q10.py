#input 12355 out=15

def CountDigit(Num):
    Sum=0
    digit=0

    while(Num!=0):
        digit=Num%10
        Sum=Sum+digit
        Num=Num//10
        
    return Sum
def main():

    print("enter first number")
    No=int(input())

    ret=CountDigit(No)

    print("Addition of digit is :",ret)


if __name__ =="__main__":
    main()