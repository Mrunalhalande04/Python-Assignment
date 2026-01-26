import threading

def Maximum(data):
    Max=0
    print("Maximum numbers:")
    for num in range(len(data)):

        if data[num] > Max:
            Max=data[num]
    print("Maximum number from list is ",Max)

def Minimum(data):
    Min=data[0]
    print("Minimum numbers:")
    for num in range(len(data)):
        if data[num] < Min:
            Min=data[num]
    print("Minimum number from list is ",Min)


def main():
    n = int(input("Enter length of list: "))
    Data = []

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
