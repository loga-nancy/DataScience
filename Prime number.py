n=10
i=2
flag=0
while i<n:
    result=n%i
    if result==0:
        flag+=1
    i+=1 
if flag==0:
    print("Prime number")
else:
    print("Not prime number")