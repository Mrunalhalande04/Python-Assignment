import threading

# global variables
sum = 0
product = 1

def Sum(data):
    global sum
    sum = 0
    for i in range(len(data)):
        sum= data[i]+sum

def Product(data):
    global product
    product = 1
    for i in range(len(data)):
        product=data[i]*product

def main():
    n = int(input("Enter length of list: "))
    Data = []

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    t1 = threading.Thread(target=Sum, args=(Data,))
    t2 = threading.Thread(target=Product, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:",sum)
    print("Product of elements:",product)

if __name__ == "__main__":
    main()
