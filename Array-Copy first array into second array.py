"""Write a Function to take an array
 and return another array that contains the members of first array that are even."""

 #Initialize array
arr1=list(input("Enter array1:"))
#Create another array arr2 with size of arr1
arr2=[None]*len(arr1)
print("Return array2 that contains same member of first array")
#Copying all elements of one array into another
def cpy(arr1,arr2):
    for i in range(0,len(arr1)):
        arr2[i]=arr1[i]
    for i in range(0,len(arr2)):
            print(arr2[i],end="")
cpy(arr1,arr2)