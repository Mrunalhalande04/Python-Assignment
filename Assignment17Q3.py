#return factorial

def Number(Num):
    fact=1

    for i in range(1,Num+1,1):
        fact=fact*i

    return fact

    
def main():

    print("Enter number :")
    No=int(input())

    ret=Number(No)

    print("Factorial is :",ret)


if __name__ =="__main__":
    main()
