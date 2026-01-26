#input 12355 out=16 

def Number(Lists):
    sum=0

    for i in range(len(Lists)):
        sum=Lists[i]+sum

    return sum

def main():

    print("Enter number of elements ")
    no=int(input())

    Data=[]
    
    print("Enter numbers :")
    for i in range(0,no):
        val=int(input())
        Data.append(val)

    ret=Number(Data)

    print("Addition of number is :",ret)




if __name__ =="__main__":
    main()