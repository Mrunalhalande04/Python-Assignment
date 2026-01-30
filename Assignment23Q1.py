class BookStore:
    NoOfBook=0

    def __init__(self,A,B):
        self.BName=A
        self.Author=B
        BookStore.NoOfBook=BookStore.NoOfBook+1

    def Display(self):
        print(f"{self.BName} by {self.Author} No of Books is {BookStore.NoOfBook}")

def main():

  

    obj1=BookStore("C Programming ","Dennis Ritchie")
    obj1.Display()

    obj2=BookStore("Linux System","Robert")
    obj2.Display()

if __name__ =="__main__":
    main()