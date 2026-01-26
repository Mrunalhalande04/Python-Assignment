import threading

def Evenfact(no):
    print("Even numbers")
    fact=0
    for i in range(1,no,1):
        if no%i==0 and i%2==0:
           print(i)
           fact=fact+i

    print("Summation of even factor are :",fact)
           

def oddfact(no):
    print("odd numbers")
    fact=0
    for i in range(1,no,1):
        if no%i==0 and i%2==1:
         print(i)
         fact=fact+i
    print("Summation of odd factor are :",fact)


def main():
   
   print("Enter number")
   no=int(input())
   
   t1=threading.Thread(target=Evenfact,args=(no,))
   t2=threading.Thread(target=oddfact,args=(no,))
   t1.start()
   t2.start()

   t1.join()
   t2.join()

if __name__ =="__main__":
    main()