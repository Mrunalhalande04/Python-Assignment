# accept two number and return maximum  number


Max=lambda Num1,Num2,Num3 :Num1 if (Num1>Num2 and Num1>Num3) else (Num2 if Num2 > Num3 else Num3)

print("Enter first number")
no1=int(input())

print("Enter second number")
no2=int(input())

print("Enter third number")
no3=int(input())

ret=Max(no1,no2,no3)

print("Maximum number is :",ret)




