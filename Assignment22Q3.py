class Arithematic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self,val1,val2):
        self.value1=val1
        self.value2=val2
        
    def Addition(self):
        return self.value1+self.value2
    
    def Substraction(self):
        return self.value1-self.value2
    
    def Multiplication(self):
        return self.value1*self.value2
    
    def Division(self):
        return self.value1 / self.value2
    
def main():

    print("Enter first number :")
    no1=int(input())

    print("Enter second number :")
    no2=int(input())

    aobj=Arithematic()
    aobj.Accept(no1,no2)

    add=aobj.Addition()
    print("Addition is :",add)

    sub=aobj.Substraction()
    print("Substraction is :",sub)

    mul=aobj.Multiplication()
    print("Multiplication is :",mul)

    div=aobj.Division()
    print("Division is :",div)


    aobj1=Arithematic()
    aobj1.Accept(no1,no2)

    add=aobj1.Addition()
    print("Addition is :",add)

    sub=aobj1.Substraction()
    print("Substraction is :",sub)

    mul=aobj1.Multiplication()
    print("Multiplication is :",mul)

    div=aobj1.Division()
    print("Division is :",div)

if __name__ =="__main__":
    main()