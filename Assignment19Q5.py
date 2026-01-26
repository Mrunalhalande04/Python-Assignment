#filter - prime number
#map =multiply by 2
#reduce =Maxzimum

from functools import reduce

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    print("Enter number of elements:")
    no = int(input())

    Data = []

    print("Enter numbers:")
    for i in range(no):
        val = int(input())
        Data.append(val)

    
    FData = list(filter(isPrime, Data))
    print("Data after filter (prime numbers):")
    print(FData)

    
    MData = list(map(lambda No: No * 2, FData))
    print("Elements after mapping (x*2):")
    print(MData)

    RData = reduce(lambda A, B: A if A > B else B, MData)
    print("Maximum element after reduce:")
    print(RData)
    
       

if __name__ == "__main__":
    main()


  
