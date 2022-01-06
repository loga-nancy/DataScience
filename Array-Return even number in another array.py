"""Write a Function to take an array and 
return another array that contains the members of first array that are even."""
#Initialize array
arr1=list(input("Enter arr1:"))
print(arr1)
#Create another array arr2 with size of arr1
arr2=[None]*len(arr1)
#Copying all elements of one array into another
def newarry(arr1,arr2):
   for i in list(range(0,len(arr1))):
      if i%2!=0:
         arr2[i]=arr1[i]
         print(arr2[i])
      
newarry(arr1,arr2)





      
