#input 1235 out=5

def Number(Lists):
    Max=0

    for i in range(len(Lists)):
        if(Lists[i] > Max):
            Max=Lists[i]


    return Max        

def main():

    print("Enter number of elements ")
    no=int(input())

    Data=[]
    
    print("Enter numbers :")
    for i in range(0,no):
        val=int(input())
        Data.append(val)

    ret=Number(Data)

    print("Maximum number is :",ret)




if __name__ =="__main__":
    main()