import Assignment17Q1mod

def main():

    print("enter first number")
    No1=int(input())

    print("Enter second number")
    No2=int(input())

    print("Addition is :",Assignment17Q1mod.Add(No1,No2))
    print("Substraction is :",Assignment17Q1mod.Sub(No1,No2))
    print("Multiplication is :",Assignment17Q1mod.Mul(No1,No2))
    print("Division is :",Assignment17Q1mod.Div(No1,No2))


if __name__ =="__main__":
    main()