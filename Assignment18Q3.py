#input 1235 out=5

def Number(Lists):
    Min=Lists[0]

    for i in range(len(Lists)):
        if(Lists[i] < Min):
            Min=Lists[i]


    return Min        

def main():

    print("Enter number of elements ")
    no=int(input())

    Data=[]
    
    print("Enter numbers :")
    for i in range(0,no):
        val=int(input())
        Data.append(val)

    ret=Number(Data)

    print("Minimum number is :",ret)




if __name__ =="__main__":
    main()