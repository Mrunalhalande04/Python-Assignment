import threading

def Even(no):
    print("Even numbers")
    Sum=0
    for i in range(1,len(no)+1):
        if i%2==0:
           print(i)
           Sum=Sum+i

    print("Summation of even are :",Sum)
           

def odd(no):
    print("odd numbers")
    Sum=0
    for i in range(1,len(no)+1):
        if i%2==1:
         print(i)
         Sum=Sum+i
    print("Summation of odd are :",Sum)


def main():
   
   print("Enter length of list")
   len=int(input())

   Data=[]
   print("enter elements in list :")

   for i in range(len):
      val=int(input())
      Data.append(val)
    
   t1=threading.Thread(target=Even,args=(Data,))
   t2=threading.Thread(target=odd,args=(Data,))
   t1.start()
   t2.start()

   t1.join()
   t2.join()

if __name__ =="__main__":
    main()