# accept two number and return Minimum  number


Min=lambda Num1,Num2 :Num1 if Num1<Num2 else Num2

print("Enter first number")
no1=int(input())

print("Enter second number")
no2=int(input())

ret=Min(no1,no2)

print("Minmum number is :",ret)
