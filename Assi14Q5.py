CheckEven=lambda no: (no%2==0) 

value=0
bret=False

print("Enter number:")
value=int(input())

bret=CheckEven(value)

if(bret==True):
    print("True")
    
else:
    print("False")


