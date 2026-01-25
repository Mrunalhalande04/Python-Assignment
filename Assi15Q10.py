def main():

    data = [10, 15, 20, 25, 30, 35, 40]

    print("Actual list is:", data)

    count = len(list(filter(lambda x: x % 2 == 0, data)))

    print("Count of even numbers is:",count)


if __name__ == "__main__":
    main()
