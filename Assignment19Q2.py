
#return power using lambda function

pow=lambda num1,num2:num1*num2

def main():
    print("Enter number ")
    no1=int(input())

    print("Enter number ")
    no2=int(input())

    ret=pow(no1,no2)

    print("Multiplication is :",ret)

if __name__ =="__main__":
    main()