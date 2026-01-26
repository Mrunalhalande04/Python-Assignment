

def Number(Lists,cnt):
    count=0
    

    for i in range(len(Lists)):
        if(Lists[i]==cnt):
            count=count+1

    return count

def main():

    print("Enter number of elements ")
    no=int(input())

    Data=[]
    
    print("Enter numbers :")
    for i in range(0,no):
        val=int(input())
        Data.append(val)

    print("Enter number that you want to count ")
    numCount=int(input())
    

    ret=Number(Data,numCount)

    print(f"count of {numCount} is {ret}")




if __name__ =="__main__":
    main()