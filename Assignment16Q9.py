#Display first 10 even number 

def Even():

    print("Even numbers are ")

    for i in range(1,21,1):
        if i%2==0:
            print(i)

def main():

    Even()
    
if __name__ =="__main__":
    main()
