#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

def Pattern(Num):

    for i in range(1,Num+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()


def main():

    print("enter first number")
    No=int(input())

    Pattern(No)


if __name__ =="__main__":
    main()