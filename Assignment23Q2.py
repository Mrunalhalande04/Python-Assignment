class BankAccount:
    ROI=10.5

    def __init__(self,A,B):
        self.Name=A 
        self.Amount=B

    def Display(self):
        print(f"Name of Account Holder is {self.Name}")
        print(f"Current Balance is {self.Amount}")

    def Deposit(self,bal):
     self.Amount=self.Amount+bal
     print("After Depositing ammount :",self.Amount)

    def Withdraw(self,amt):
        withdrawamt=0
        max=2000
       
        if(amt > max):
            withdrawamt=self.Amount-amt
            print(f"Successfully Withdraw {withdrawamt}")

        else:
            print("Insufficient Balance...")

    def CalculateInterest(self):
        return self.Amount*BankAccount.ROI / 100       
    


def main():

    bobj=BankAccount("Mrunal",1000)
    bobj.Display()
    
    print("Enter ammount to Deposit :")
    add=int(input())
    bobj.Deposit(add)

    print("Enter Amount to withdraw :")
    sub=int(input())
    bobj.Withdraw(sub)

    ret=bobj.CalculateInterest()
    print("interest is :",ret)


if __name__ =="__main__":
    main()