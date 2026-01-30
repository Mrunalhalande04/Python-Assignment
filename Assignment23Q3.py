class Number:

    def __init__ (self,value):
        self.no=value

    def ChkPrime(self):
        if self.no <= 1:
          return False

        count = 0
        for i in range(1, self.no + 1):
          if (self.no % i == 0):
            count =count+1

        return count == 2

        
    def ChkPerfect(self):
        sum=0

        for i in range(1,self.no):
            if (self.no % i == 0):
                sum=sum+i

        return sum==self.no
            
    def Factors(self):
        fact=0

        for i in range(1,self.no):
            if (self.no%i==0):
                print(i)

    def SumFactors(self): 
        sum=0

        for i in range(1,self.no):
            if (self.no %i ==0):
                sum=sum+i
        
        return sum

def main():
    ino=int(input("Enter number :"))

    nobj=Number(ino)

    iret=nobj.ChkPrime()
    if(iret==True):
        print("Number is prime ")

    else:
        print("Number is not prime")

    
    iret=nobj.ChkPerfect()
    if(iret==True):
        print("Number is Perfect ")

    else:
        print("Number is not Perfect")

    nobj.Factors()

    sum=nobj.SumFactors()
    print("Summation of factors is :",sum)

if __name__ =="__main__":
    main()