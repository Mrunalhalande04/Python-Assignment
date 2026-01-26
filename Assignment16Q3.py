#add two number

def Addition(Num1,Num2):
    sum=0

    sum=Num1+Num2

    return sum



def main():
    
    print("Enter number :")
    No1=int(input())

    print("Enter number :")
    No2=int(input())


    ret=Addition(No1,No2)

    print("Addition is :",ret)


if __name__ =="__main__":
    main()
