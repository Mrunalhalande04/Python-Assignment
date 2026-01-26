def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def prime(Lists):
    Sum = 0
    for i in Lists:
        if isPrime(i):
            Sum += i
    return Sum

