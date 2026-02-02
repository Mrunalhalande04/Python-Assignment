import os

def ChkFile(FileName):
    if os.path.exists(FileName):
        return True
    else:
        return False

def main():
    name = input("Enter file name that you want to check ")
    ret = ChkFile(name)

    if ret:
        print("File Exists")
    else:
        print("File Does Not Exist")

if __name__ == "__main__":
    main()
