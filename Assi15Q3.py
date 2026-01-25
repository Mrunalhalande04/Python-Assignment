
def main():

    List=[2,3,4,5,6,7,8,9]

    print("Actual data is :",List)
    
    print("Data after filter is :")
    result=list(filter((lambda No:No%2==1),List)) 
    print("Odd number from list are :",result)

    
if __name__ =="__main__":
    main()