from functools import reduce

def main():

    List=[1,2,3,4,8,5]

    print("Actual data is :",List)
 
    print("Elements after reduce :")
    Result=reduce((lambda A, B: A if A < B else B),List)
    print("Addition is :",Result)


if __name__ =="__main__":
    main()