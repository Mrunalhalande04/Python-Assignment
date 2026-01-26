#check number is positive negative or zero

def Number(Num):

    if Num<0:
        print("Negative Number")

    elif Num==0:
        print("Zero")

    else:
        print("Posituve number")


def main():

    print("Enter number :")
    No=int(input())

    Number(No)


if __name__ =="__main__":
    main()
