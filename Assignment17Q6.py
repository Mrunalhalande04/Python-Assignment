#   * * * * * 
#   * * * * 
#   * * * 
#   * * 
#   * 

def Pattern(Num):

    for i in range(Num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


def main():

    print("enter first number")
    No=int(input())

    Pattern(No)


if __name__ =="__main__":
    main()