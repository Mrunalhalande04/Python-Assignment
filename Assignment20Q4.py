import threading

def Capital(data):
    count=0
    for i in range(len(data)):
        if(data[i]>='A' and data[i]<='Z'):
            count=count+1
    print("Thread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Summation of capital letter in string is :",count)

def Small(data):
    count=0
    for i in range(len(data)):
        if(data[i]>='a' and data[i]<='z'):
            count=count+1

    print("Thread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Summation of small letter in string is :",count)

def Digit(data):
    count=0
    for i in range(len(data)):
        if data[i].isdigit():
            count=count+1
    print("Thread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Summation of digit in string is :",count)


def main():
   
   print("Enter number")
   strs=input()
   
   t1=threading.Thread(target=Capital,args=(strs,))
   t2=threading.Thread(target=Small,args=(strs,))
   t3=threading.Thread(target=Digit,args=(strs,))
   
   t1.start()
   t2.start()
   t3.start()

   t1.join()
   t2.join()
   t3.join()

if __name__ =="__main__":
    main()