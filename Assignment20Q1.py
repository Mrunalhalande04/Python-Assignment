import threading

def Even():
    print("Even numbers")
    for i in range(1,20+1,1):
        if i%2==0:
         print(i)

def odd():
    print("odd numbers")
    for i in range(1,20+1,1):
        if i%2==1:
         print(i)


def main():
   
   t1=threading.Thread(target=Even,args=())
   t1.start()
   t2=threading.Thread(target=odd,args=())
   t2.start()

   t1.join()
   t2.join()

if __name__ =="__main__":
    main()