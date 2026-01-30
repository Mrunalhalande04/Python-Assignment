class Arithematic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        self.value1=int(input("Enter first number "))
        self.value2=int(input("Enter second number "))
        
    def Addition(self):
        return self.value1+self.value2
    
    def Substraction(self):
        return self.value1-self.value2
    
    def Multiplication(self):
        return self.value1*self.value2
    
    def Division(self):
        return self.value1 / self.value2
    
def main():


    aobj=Arithematic()
    aobj.Accept()

    add=aobj.Addition()
    print("Addition is :",add)

    sub=aobj.Substraction()
    print("Substraction is :",sub)

    mul=aobj.Multiplication()
    print("Multiplication is :",mul)

    div=aobj.Division()
    print("Division is :",div)


    aobj1=Arithematic()
    aobj1.Accept()

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
