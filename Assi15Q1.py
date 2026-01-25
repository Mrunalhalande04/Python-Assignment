
def main():

    List=[5,10,7,3,9,4]

    print("Actual data is :",List)
    
    print("Elements after mapping :")
    result=list(map((lambda No:No*No),List))
    print("Square of each number is :",result)
   

if __name__ =="__main__":
    main()