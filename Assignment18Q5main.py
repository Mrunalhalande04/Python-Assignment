import Assignment18Q5mod

def main():
    print("Enter number ")
    no=int(input())

    Data=[]

    for i in range(no):
        val=int(input())
        Data.append(val)

    print("Sum of prime number is :",Assignment18Q5mod.prime(Data))



if __name__ =="__main__":
    main()