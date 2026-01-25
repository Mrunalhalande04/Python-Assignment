def main():

    data = ["python", "java", "programming", "code", "developer"]

    print("Actual list is:", data)

    result = list(filter(lambda s: len(s) > 5, data))

    print("Strings having length greater than 5:", result)


if __name__ == "__main__":
    main()
