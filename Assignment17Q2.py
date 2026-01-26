
def Pattern(Num):

    for i in range(Num):
        for j in range(Num):
            print("*",end=" ")

        print()

def main():

    print("enter first number")
    No=int(input())

    Pattern(No)


if __name__ =="__main__":
    main()