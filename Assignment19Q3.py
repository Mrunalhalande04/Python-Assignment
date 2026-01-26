from functools import reduce

def main():

    print("Enter number of elements ")
    no=int(input())

    Data=[]
    
    print("Enter numbers :")
    for i in range(0,no):
        val=int(input())
        Data.append(val)

    print("Data after filter is :")
    FData=list(filter((lambda No:No>=70 and No<=90),Data)) 
    print(FData)

    print("Elements after mapping :")
    MData=list(map((lambda No:No+10),FData))
    print(MData)

    print("Elements after reduce :")
    RData=reduce((lambda A,B:A*B),MData)
    print(RData)

if __name__ =="__main__":
    main()



  
