num=int(input("Enter a nmber:"))
flag=0
a=0
b=1
if num<0:
    print("Please enter positive number")
elif num==1:
    print(a)
else:
    print("Fibonacci series:")
    print(a)
    print(b)
    while flag<num:
        c=a+b
        a=b
        b=c
        flag=flag+1
        print(c)
  

