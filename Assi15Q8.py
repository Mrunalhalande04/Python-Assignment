def main():

    List=[2,3,4,5,6,7,8,9,15]

    print("Actual data is :",List)
    
    print("Data after filter is :")
    result=list(filter((lambda No:No%3==0 and No%5==0),List)) 
    print("divisible by 5 and 3 :",result)

    
if __name__ =="__main__":
    main()