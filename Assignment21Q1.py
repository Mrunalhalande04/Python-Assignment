import threading

def Prime(data):
    print("Prime numbers:")
    for num in data:
        if is_prime(num):
            print(num)

def Non_Prime(data):
    print("Non-prime numbers:")
    for num in data:
        if num > 1 and not is_prime(num):
            print(num)

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main():
    n = int(input("Enter length of list: "))
    Data = []

    print("Enter elements:")
    for i in range(n):
        Data.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=Non_Prime, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
