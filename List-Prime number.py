#Print prime numbers in given array

#create a empty list for input
my_list=[]
#number of elements as input
n=int(input("Enter number of elements:"))
#iterate till the range
for i in range(0,n):
    element=int(input())
    my_list.append(element) # adding element to list
print(my_list)
#create a empty list for output
prime=[]
#iterate list
for i in my_list:
    flag=0
    for j in range(2,i): #iterate each ele in list
        if i%j==0:
            flag=flag+1
    if flag==0:
        prime.append(i)
print(prime)