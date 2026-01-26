#input 12345 out=5

def CountDigit(Num):
    count=0

    while(Num!=0):
        count=count+1
        Num=Num//10
    return count
def main():

    print("enter first number")
    No=int(input())

    ret=CountDigit(No)

    print("Count of digit :",ret)


if __name__ =="__main__":
    main()